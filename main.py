import streamlit as st
import os
import torch
from classifier import classify_clothing
from llm import explain_outfit
from utils import preprocess_image
from faiss_db import VectorDB
from torchvision.models import resnet50, ResNet50_Weights
from outfit_suggester import generate_outfit
from collections import Counter

# Directories
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Load pretrained ResNet50 as feature extractor
weights = ResNet50_Weights.DEFAULT
resnet = resnet50(weights=weights)
resnet.fc = torch.nn.Identity()
resnet.eval()

vdb = VectorDB(dim=2048)

st.title("👚 Virtual Closet: AI Outfit Recommender")

# --- Upload UI
uploaded_file = st.file_uploader("Upload a clothing image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    filepath = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(filepath, caption="Uploaded Image", use_container_width=True)

    # --- Classification
    try:
        label = classify_clothing(filepath)
        st.success(f"Predicted: **{label}**")
    except Exception as e:
        st.error(f"Classification failed: {e}")
        st.stop()

    # --- Feature Extraction
    try:
        img_tensor = preprocess_image(filepath)
        with torch.no_grad():
            embedding = resnet(img_tensor).squeeze().numpy()
        vdb.add_item(embedding, label)
        st.info("Item added to virtual closet!")
    except Exception as e:
        st.error(f"Embedding failed: {e}")
        st.stop()

# --- Outfit Suggestion Section
st.markdown("---")
st.subheader("🧠 Outfit Suggestion")

weather = st.selectbox("Select Weather", ["sunny", "cold", "rainy"])
event = st.selectbox("Select Event", ["casual", "formal", "party"])



if st.button("Generate Outfit"):
    try:
        closet_items = vdb.metadata
        results = generate_outfit(closet_items, weather, event)

        # ✅ Clean and deduplicate results after they exist  x
         
         # ✅ NOW SAFE: results is defined above
        cleaned_items = []
        for label in results:
            main_label = label.split(",")[0].strip().lower()
            cleaned_items.append(main_label)
        unique_items = list(dict.fromkeys(cleaned_items))[:3]

        explanation = explain_outfit(unique_items, weather, event)

        # ✅ Output
        st.markdown("### 👗 Suggested Outfit:")
        for item in unique_items:
            st.markdown(f"- {item.title()}")

        st.markdown("### 🤖 AI's Explanation:")
        st.write(explanation)

    except Exception as e:
        st.error(f"Error generating outfit: {e}")
