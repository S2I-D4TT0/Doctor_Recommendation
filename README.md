# **Doctor Recommendation System**

This **Streamlit** app provides **AI-based doctor recommendations** based on patient symptoms using **SBERT embeddings** and **cosine similarity**.

## 🌟 **Features**

✅ **Search doctors by symptoms using AI**  
✅ **Filter by medical specialties**  
✅ **Interactive and user-friendly UI**  
✅ **Real-time doctor recommendations**  
✅ **Doctor profile photos and key details**  
✅ **"Explore Doctors" and "Ask AI for Recommendations" sections**  

## 🖥️ **Live Demo**

Check out the live demo: [Doctor Recommendation System](https://doctorrecommendation-cwbuqysehqcnj5kemxhgsk.streamlit.app/)

## 📚 **Tech Stack**

- **Frontend:** Streamlit (for a clean and intuitive UI)
- **AI Models:** SBERT (Sentence-BERT) for computing similarity
- **Similarity Metric:** Cosine Similarity for query embeddings 

## 🚀 **How to Run the App Locally**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/S2I-D4TT0/Doctor_Recommendation.git
   cd Doctor_Recommendation
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

5. **Access the app** at `http://localhost:8501` in your web browser.

## 📊 **How It Works**

1. **Data Processing:** Doctor profiles are loaded from `data.xlsx` and embedded using **SBERT** for efficient similarity matching.
2. **User Input:** Users enter symptoms, and the system encodes their input.
3. **Similarity Calculation:** **Cosine similarity** is computed between the input and doctor embeddings.
4. **Ranking:** Doctors are ranked based on similarity scores, prioritizing high-level qualifications (e.g., MD).
5. **Display:** Recommended doctors, including profiles and specializations, are displayed in a user-friendly format.

## 📦 **Folder Structure**

```
Doctor_Recommendation/
├── app.py                 # Main Streamlit application
├── data.xlsx              # Doctor dataset (Excel format)
└── README.md              # Project documentation
```

## 🛠️ **Customization**

- **Add New Doctors:** Update the dataset in the `data.xlsx` file.
- **Model Tuning:** Replace SBERT with other embeddings in `app.py`.

## 🤝 **Contributing**

Contributions are welcome! Feel free to open an issue or submit a pull request.
