import streamlit as st
import cv2
import numpy as np
from PIL import Image
from colour_analysis import color_harmony_score
from composition_score import composition_score
from emotion_estimator import emotion_score


st.set_page_config(page_title="AIrt Critic 🎨", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .reportview-container {
        background: linear-gradient(120deg, #f6f9fc, #e9f0ff);
        color: #000000;
    }
    .stButton>button {
        background-color: #6c63ff;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stButton>button:hover {
        background-color: #554bf2;
    }
    .stFileUploader {
        background-color: white;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("About")
    st.info("Upload any painting, drawing, or digital art, and this app will rate its **composition**, **color harmony**, and **emotional feel** using basic visual rules.")
    st.markdown("---")
    st.caption("Created by Saranyaa")


st.title("🧠 AIrt Critic")
st.subheader("Upload your art and get a full aesthetic evaluation!")

uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_pil = Image.open(uploaded_file).convert("RGB")
    st.image(image_pil, caption="🎨 Your Uploaded Artwork", use_container_width=True)
    
    image_np = np.array(image_pil)
    image_cv2 = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    if st.button("🎯 Critique My Art"):
        with st.spinner("Analyzing... 🎨🧠"):
            color_score = color_harmony_score(image_cv2)
            comp_score = composition_score(image_cv2)
            emotion = emotion_score(image_cv2)
            final_score = round((color_score + comp_score) / 2, 1)

        st.success("✅ Done! Here's your analysis:")

        
        st.markdown(f"### 🎨 Color Harmony — **{color_score}/10**")
        st.progress(color_score / 10)

        st.markdown(f"### 📐 Composition — **{comp_score}/10**")
        st.progress(comp_score / 10)

        st.markdown("### 🧠 Detected Emotion")
        st.info(f"**{emotion}**")

        st.markdown("### 🎖 Final Aesthetic Score")
        st.metric(label="Score out of 10", value=final_score)

        
        st.markdown("---")
        if final_score >= 9:
            st.success("🌟 *Masterpiece!* The image achieves near-perfect harmony and structure.")
        elif final_score >= 7:
            st.info("✨ *Very Good!* There's a strong sense of visual appeal.")
        elif final_score >= 5:
            st.warning("📌 *Average*. Some aspects could be improved.")
        else:
            st.error("🧱 *Needs Work.* Try adjusting color balance or focal points.")
