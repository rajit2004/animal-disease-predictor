# 🐾 Animal Disease Prediction System

> An ML-powered web app that predicts probable animal diseases based on symptom severity — with probability insights, confidence scoring, PDF reports, and case tracking.

[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-brightgreen?style=for-the-badge&logo=streamlit)](https://animal-disease-predictor.streamlit.app/)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/rajit2004?style=for-the-badge&logo=githubsponsors&color=EA4AAA)](https://github.com/sponsors/rajit2004)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![ML](https://img.shields.io/badge/ML-Random%20Forest-orange?style=flat)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?style=flat)

---

## 🌍 Live Demo

🔗 **[animal-disease-predictor.streamlit.app](https://animal-disease-predictor.streamlit.app/)**

> No installation needed — open the link and start predicting!

---

## 📸 Screenshots

**Main Interface**
<img src="screenshots/Screenshot%202026-04-23%20111257.png" width="700"/>

**Prediction Result**
<img src="screenshots/Screenshot%20(25).png" width="700"/>

**Results & Case History**
<img src="screenshots/Screenshot%20(26).png" width="700"/>

**PDF Report**
<img src="screenshots/Screenshot%202026-04-23%20113302.png" width="700"/>

---

## 🚀 Features

- 🔢 **Severity-based symptom input** — rate each symptom from 0 (None) to 3 (Severe)
- 🤖 **Random Forest classifier** — multi-class ML model for disease prediction
- 📊 **Probability distribution chart** — see confidence levels across all diseases
- 🎯 **Confidence scoring** — High / Moderate / Low rating per prediction
- 📄 **Downloadable PDF report** — shareable diagnostic summary
- 🐶 **Multi-animal profile support** — Name, Species, Age
- 🕒 **Timestamped case logging** — every prediction is tracked
- 📁 **Case history tracking** — review past diagnoses

---

## 🧠 How It Works

```
User inputs symptom severity values (0–3)
        ↓
Random Forest Classifier processes inputs
        ↓
Predicts disease with probability scores
        ↓
Generates PDF report + logs to case history
```

**Model details:**
- Algorithm: Random Forest Classifier
- Type: Supervised Multi-Class Classification
- Input: Symptom severity ratings
- Output: Predicted disease + probability distribution

---

## 🏥 Diseases Covered

| Disease | Type |
|---|---|
| Parvovirus | Viral |
| Gastroenteritis | Digestive |
| Kennel Cough | Respiratory |
| Lyme Disease | Bacterial |
| Feline Upper Respiratory Infection | Viral |
| Healthy | — |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| ML Model | Scikit-learn (Random Forest) |
| Data | Pandas |
| PDF Generation | FPDF2 |
| Visualization | Matplotlib |
| Model Serialization | Joblib |

---

## 📂 Project Structure

```
animal-disease-predictor/
├── app.py                 # Main Streamlit application
├── model.pkl              # Trained ML model
├── animal_disease.csv     # Training dataset
├── requirements.txt       # Dependencies
└── README.md
```

---

## ⚡ Run Locally

```bash
git clone https://github.com/rajit2004/animal-disease-predictor.git
cd animal-disease-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 💖 Support This Project

This project is completely free and open source. If you found it useful or want to support more projects like this:

[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/rajit2004)

---

## 👨‍💻 Author

**Ranesh Rajit** — B.Tech CS Student, India

[![GitHub](https://img.shields.io/badge/GitHub-rajit2004-black?style=flat&logo=github)](https://github.com/rajit2004)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-ranesh--kun-blue?style=flat&logo=linkedin)](https://linkedin.com/in/ranesh-kun)
