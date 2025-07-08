import os
from dotenv import load_dotenv
from transformers import pipeline
import streamlit as st

# Load token from .env
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

@st.cache_resource
def load_llm():
    if not hf_token:
        st.error("Please set HUGGINGFACEHUB_API_TOKEN in your .env file")
        return None
    
    try:
        llm_pipeline = pipeline(
            "text2text-generation",
            model="google/flan-t5-small",
            token=hf_token
        )
        return llm_pipeline
    except Exception as e:
        st.error(f"Error loading LLM: {e}")
        return None

def explain_outfit(items, weather, event):
    llm = load_llm()  # ✅ load the model here
    if llm is None:
        return "LLM could not be loaded."

    outfit_list = ", ".join(items)
    prompt = (
        f"You are a fashion stylist. Suggest an outfit using these items: {outfit_list}. "
        f"The outfit should be suitable for {weather} weather and a {event} event. "
        f"Explain why each piece was chosen."
    )

    try:
        response = llm(prompt, max_new_tokens=100, do_sample=False)
        return response[0]['generated_text']
    except Exception as e:
        st.error(f"Error generating explanation: {e}")
        return "Sorry, could not generate explanation."
