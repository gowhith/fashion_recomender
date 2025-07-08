import os
from dotenv import load_dotenv
load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import torch
import streamlit as st

# Cache the models to avoid reloading
@st.cache_resource
def load_classification_model():
    if not hf_token:
        st.error("Please set HUGGINGFACEHUB_API_TOKEN in your .env file")
        return None, None
    
    try:
        extractor = AutoFeatureExtractor.from_pretrained(
            "facebook/deit-base-distilled-patch16-224", 
            token=hf_token
        )
        model = AutoModelForImageClassification.from_pretrained(
            "facebook/deit-base-distilled-patch16-224", 
            token=hf_token
        )
        model.eval()
        return extractor, model
    except Exception as e:
        st.error(f"Error loading classification model: {e}")
        return None, None

def classify_clothing(image_path):
    extractor, model = load_classification_model()
    
    if extractor is None or model is None:
        return "Unknown"
    
    try:
        image = Image.open(image_path).convert("RGB")
        inputs = extractor(images=image, return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits
        predicted_class_idx = logits.argmax(-1).item()
        label = model.config.id2label[predicted_class_idx]
        return label
    except Exception as e:
        st.error(f"Error classifying image: {e}")
        return "Unknown"