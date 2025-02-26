import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
doctors_df = pd.read_excel('task_actual_dataset.xlsx', sheet_name='Doctors')

# Data cleaning
doctors_df['doctor_name'] = doctors_df['name'].str.split(',').str[0].str.strip()
doctors_df['specialties'] = doctors_df['specialties'].str.replace('', '').str.strip()
doctors_df['location'] = doctors_df['location'].str.replace('', '').str.strip()
doctors_df['combined_text'] = doctors_df['specialties'] + ' ' + doctors_df['overview']

doctors_df['location'] = doctors_df['location'].str.replace(' ', ', ', n=1)

# Load SBERT model
sbert_model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for doctor profiles
doctor_embeddings = sbert_model.encode(doctors_df['combined_text'].tolist(), show_progress_bar=True)

# Function to recommend doctors
def recommend_doctors(query, top_n=5):
    query_embedding = sbert_model.encode([query])
    similarities = cosine_similarity(query_embedding, doctor_embeddings).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return doctors_df.iloc[top_indices][['doctor_name', 'specialties', 'location', 'profile_link']], similarities[top_indices]

# 🌟 Streamlit UI 🌟
st.set_page_config(page_title="AI Doctor Finder", layout="wide")

# 💙 Header Section
st.markdown("""
    <div style="text-align: center; font-size: 42px; font-family: 'Helvetica Neue', sans-serif; color: #FFFFFF; background-color: #2C3E50; padding: 30px; border-radius: 20px;">
        🧑‍⚕️ <b>AI Doctor Finder</b> 🏥
    </div>
""", unsafe_allow_html=True)

# Sidebar for AI Recommendation
st.sidebar.header("🤖💬 AI Doctor Recommendation")
query = st.sidebar.text_input("Describe your symptoms:", placeholder="E.g., I have severe headaches and migraines")
top_n = st.sidebar.slider("Number of recommendations:", min_value=1, max_value=10, value=5)

if st.sidebar.button("🔎 Find My Doctor"):
    if query:
        with st.spinner("🔄 Processing your request..."):
            recommended_doctors, scores = recommend_doctors(query, top_n)
        st.sidebar.markdown("### 👨‍⚕️ Recommended Doctors")

        for i, (index, row) in enumerate(recommended_doctors.iterrows()):
            st.sidebar.markdown(f"""
                <div style="border-radius: 15px; font-family: 'Helvetica Neue', sans-serif; background: #34495E; padding: 15px; margin-bottom: 15px;">
                    <h4 style="color: #ECF0F1;">{i+1}. {row['doctor_name']}</h4>
                    <p><b>🩺 Specialties:</b> <span style="color: #BDC3C7;">{row['specialties']}</span></p>
                    <p><b>📍 Location:</b> <span style="color: #BDC3C7;">{row['location']}</span></p>
                    <p><b>🔗 <a href="{row['profile_link']}" target="_blank" style="color: #1ABC9C;">View Profile</a></b></p>
                    <p><b>⭐ Match Score:</b> {scores[i]:.4f}</p>
                </div>
            """, unsafe_allow_html=True)

            if top_n == 1:
                break

        st.markdown("<style>section.main {height: 120vh; overflow-y: auto;}</style>", unsafe_allow_html=True)
    else:
        st.sidebar.warning("⚠️ Please enter your symptoms before searching.")

# 📌 Filter Section
st.markdown("## 🔎 Explore Doctors by Specialties")
specialties = doctors_df['specialties'].unique().tolist()
selected_specialty = st.selectbox("Choose a specialty:", ["All"] + specialties)

if selected_specialty == "All":
    filtered_df = doctors_df
else:
    filtered_df = doctors_df[doctors_df['specialties'] == selected_specialty]

# 🎯 Display Doctors
for i, row in filtered_df.iterrows():
    st.markdown(f"""
        <div style="border-radius: 15px; font-family: 'Helvetica Neue', sans-serif; background: #1C2833; padding: 15px; margin-bottom: 15px;">
            <h3 style="color: #ECF0F1;">👨‍⚕️ {row['doctor_name']}</h3>
            <p><b>🩺 Specialties:</b> <span style="color: #BDC3C7;">{row['specialties']}</span></p>
            <p><b>📍 Location:</b> <span style="color: #BDC3C7;">{row['location']}</span></p>
            <p><b>🔗 <a href="{row['profile_link']}" target="_blank" style="color: #1ABC9C;">View Doctor Profile</a></b></p>
        </div>
    """, unsafe_allow_html=True)

# 🎨 Footer
st.markdown("""
    <div style="text-align: center; font-size: 24px; font-family: 'Helvetica Neue', sans-serif; color: #ECF0F1; background-color: #1C2833; padding: 15px; border-radius: 15px;">
        Made with ❤️ by AI & Streamlit 🚀
    </div>
""", unsafe_allow_html=True)
