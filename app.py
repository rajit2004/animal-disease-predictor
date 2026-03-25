import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
from fpdf import FPDF
from datetime import datetime
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(page_title="Animal Disease Prediction", layout="centered")

# ---------------- LOAD MODEL & DATA ----------------

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

@st.cache_data
def load_data():
    data = pd.read_csv("animal_disease.csv")
    X = data.drop("Disease", axis=1)
    y = data["Disease"]
    return X, y

model = load_model()
X, y = load_data()
accuracy = accuracy_score(y, model.predict(X))

# ---------------- SESSION STATE INIT ----------------

default_values = {
    "fever": 0,
    "cough": 0,
    "diarrhea": 0,
    "lethargy": 0,
    "loss": 0
}

for key, val in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = val

if "prediction" not in st.session_state:
    st.session_state.prediction = None
    st.session_state.probabilities = None
    st.session_state.confidence = None
    st.session_state.symptoms = None
    st.session_state.timestamp = None
    st.session_state.case_data = None

# ---------------- RESET FUNCTION ----------------

def reset_fields():
    for key in default_values:
        st.session_state[key] = 0

    st.session_state.prediction = None
    st.session_state.probabilities = None
    st.session_state.confidence = None
    st.session_state.symptoms = None
    st.session_state.timestamp = None

# ---------------- HEADER ----------------

st.title("🐾 Animal Disease Prediction System")
st.write("Enter animal details and adjust symptom severity.")

# ---------------- SIDEBAR ----------------

st.sidebar.header("Model Information")
st.sidebar.write("Algorithm: Random Forest")
st.sidebar.write(f"Model Accuracy: {round(accuracy * 100, 2)}%")

st.sidebar.markdown("---")
st.sidebar.subheader("Severity Scale")
st.sidebar.write("0 → None")
st.sidebar.write("1 → Mild")
st.sidebar.write("2 → Moderate")
st.sidebar.write("3 → Severe")

# ---------------- ANIMAL PROFILE ----------------

st.subheader("Animal Profile")

animal_name = st.text_input("Animal Name / ID")
species = st.selectbox("Species", ["Dog", "Cat", "Other"])
age = st.number_input("Age (years)", 0, 30, 0)

# ---------------- SYMPTOM FORM ----------------

st.subheader("Symptom Severity")

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        st.slider("Fever", 0, 3, key="fever")
        st.slider("Cough", 0, 3, key="cough")
        st.slider("Diarrhea", 0, 3, key="diarrhea")

    with col2:
        st.slider("Lethargy", 0, 3, key="lethargy")
        st.slider("Loss of Appetite", 0, 3, key="loss")

    submit = st.form_submit_button("Predict Disease")

# ---------------- SEVERITY DISPLAY ----------------

total_severity = (
    st.session_state.fever +
    st.session_state.cough +
    st.session_state.diarrhea +
    st.session_state.lethargy +
    st.session_state.loss
)

if total_severity == 0:
    st.success("Overall Severity Level: Minimal")
elif total_severity <= 4:
    st.info("Overall Severity Level: Mild")
elif total_severity <= 8:
    st.warning("Overall Severity Level: Moderate")
else:
    st.error("Overall Severity Level: Severe")

st.button("Reset All Symptoms", on_click=reset_fields)

# ---------------- PREDICTION ----------------

if submit and animal_name.strip() != "":

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    input_data = pd.DataFrame(
        [[
            st.session_state.fever,
            st.session_state.cough,
            st.session_state.diarrhea,
            st.session_state.lethargy,
            st.session_state.loss
        ]],
        columns=X.columns
    )

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    confidence = max(probabilities)

    st.session_state.prediction = prediction
    st.session_state.probabilities = probabilities
    st.session_state.confidence = confidence
    st.session_state.timestamp = timestamp
    st.session_state.symptoms = {
        "Fever": st.session_state.fever,
        "Cough": st.session_state.cough,
        "Diarrhea": st.session_state.diarrhea,
        "Lethargy": st.session_state.lethargy,
        "Loss of Appetite": st.session_state.loss
    }

    # Save case history
    case_record = {
        "Timestamp": timestamp,
        "Animal_Name": animal_name,
        "Species": species,
        "Age": age,
        **st.session_state.symptoms,
        "Prediction": prediction,
        "Confidence": confidence
    }

    file_exists = os.path.isfile("case_history.csv")
    pd.DataFrame([case_record]).to_csv(
        "case_history.csv",
        mode="a",
        header=not file_exists,
        index=False
    )

# ---------------- DISPLAY RESULTS ----------------

if st.session_state.prediction is not None:

    prediction = st.session_state.prediction
    confidence = st.session_state.confidence
    timestamp = st.session_state.timestamp

    st.success(f"### Predicted Disease: {prediction}")
    st.write(f"🕒 Timestamp: {timestamp}")

    if confidence > 0.75:
        st.success(f"High Confidence: {round(confidence, 3)}")
    elif confidence > 0.5:
        st.warning(f"Moderate Confidence: {round(confidence, 3)}")
    else:
        st.error(f"Low Confidence: {round(confidence, 3)}")

    st.subheader("Clinical Interpretation")

    for key, value in st.session_state.symptoms.items():
        st.write(f"• {key}: {value}")

    st.write(
        "The presented symptom pattern aligns with statistical patterns "
        "associated with the predicted condition. Further clinical examination "
        "is recommended for confirmation."
    )

    # ---------------- SIMPLE PDF (TEXT ONLY) ----------------

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Animal Disease Prediction Report", ln=True, align="C")
    pdf.ln(5)

    pdf.cell(200, 10, txt=f"Timestamp: {timestamp}", ln=True)
    pdf.cell(200, 10, txt=f"Animal: {animal_name}", ln=True)
    pdf.cell(200, 10, txt=f"Species: {species}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt=f"Predicted Disease: {prediction}", ln=True)
    pdf.cell(200, 10, txt=f"Confidence: {round(confidence, 3)}", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt="Symptom Severity:", ln=True)
    for key, value in st.session_state.symptoms.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf_output = bytes(pdf.output(dest="S"))

    st.download_button(
        label="Download PDF Report",
        data=pdf_output,
        file_name=f"{animal_name}_report.pdf",
        mime="application/pdf"
    )

# ---------------- CASE HISTORY ----------------

st.markdown("---")
st.subheader("Case History")

if os.path.isfile("case_history.csv"):
    history_df = pd.read_csv("case_history.csv")
    st.dataframe(history_df.tail(10))
else:
    st.write("No cases recorded yet.")
