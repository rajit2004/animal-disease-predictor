# 🐾 Animal Disease Prediction System

An intelligent machine learning-based web application that predicts probable animal diseases based on symptom severity inputs.

Built using **Python, Scikit-learn, and Streamlit**, this system serves as a diagnostic support tool for early-stage disease identification.

---
## 🌍 Live Demo

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-brightgreen)](https://animal-disease-predictor.streamlit.app/)

## 🚀 Features

- 🔢 Severity-based symptom input (0 = None → 3 = Severe)
- 🤖 Random Forest multi-class classification model
- 📊 Probability distribution visualization
- 🎯 Confidence scoring (High / Moderate / Low)
- 📄 Downloadable PDF diagnostic report
- 🐶 Multi-animal profile support (Name, Species, Age)
- 🕒 Timestamped case logging
- 📁 Case history tracking

---

## 🧠 Machine Learning

- Algorithm: Random Forest Classifier  
- Type: Supervised Multi-Class Classification  
- Input: Symptom severity values  
- Output: Predicted disease with probabilities  

---

## 🏥 Diseases Covered

- Parvovirus  
- Gastroenteritis  
- Kennel Cough  
- Lyme Disease  
- Feline Upper Respiratory Infection  
- Healthy  

---

## 🖥️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- Joblib  
- FPDF2  
- Matplotlib  

---

## 📂 Project Structure
AnimalDisease/
│── app.py # Main Streamlit application
│── model.pkl # Trained ML model
│── animal_disease.csv # Dataset
│── case_history.csv # Stored predictions
│── requirements.txt # Dependencies

---


---

## ⚡ Installation & Setup

```bash
git clone https://github.com/rajit2004/animal-disease-predictor.git
cd animal-disease-predictor
pip install -r requirements.txt
streamlit run app.py
