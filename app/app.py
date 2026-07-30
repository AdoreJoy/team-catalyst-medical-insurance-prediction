import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------
st.set_page_config(page_title="Insurance Cost Predictor", page_icon="💰", layout="centered")

st.title("💰 Medical Insurance Cost Predictor")
st.write(
    "Team Catalyst — enter your details below to get an estimated annual "
    "medical insurance charge, based on our trained Random Forest model."
)

# ---------------------------------------------------------------
# Load the trained model and the exact column order it expects
# ---------------------------------------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("model.pkl")
    columns = joblib.load("model_columns.pkl")
    return model, columns

model, model_columns = load_model()

# ---------------------------------------------------------------
# Input form
# ---------------------------------------------------------------
st.subheader("Your details")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", min_value=18, max_value=100, value=30)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    children = st.number_input("Number of children", min_value=0, max_value=10, value=0, step=1)

with col2:
    sex = st.selectbox("Sex", ["Female", "Male"])
    smoker = st.selectbox("Smoker?", ["No", "Yes"])
    region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

predict_button = st.button("Predict my insurance cost", type="primary")

# ---------------------------------------------------------------
# Build the feature vector to match training-time encoding exactly
# ---------------------------------------------------------------
def build_feature_row(age, sex, bmi, children, smoker, region, model_columns):
    # Start every column at 0, then fill in what applies —
    # this guarantees the same column order/names the model was trained on
    row = {col: 0 for col in model_columns}

    row["age"] = age
    row["bmi"] = bmi
    row["children"] = children

    # One-hot columns — only set to 1 if that column exists in model_columns
    # (drop_first=True during training means one category per group has no column at all)
    if "sex_male" in row and sex == "Male":
        row["sex_male"] = 1

    smoker_flag = 1 if smoker == "Yes" else 0
    if "smoker_yes" in row:
        row["smoker_yes"] = smoker_flag

    region_col = f"region_{region.lower()}"
    if region_col in row:
        row[region_col] = 1

    # Interaction terms, matching training-time feature engineering
    if "bmi_x_smoker" in row:
        row["bmi_x_smoker"] = bmi * smoker_flag
    if "age_x_smoker" in row:
        row["age_x_smoker"] = age * smoker_flag

    # Return as a single-row DataFrame in the exact column order the model expects
    return pd.DataFrame([row])[model_columns]

# ---------------------------------------------------------------
# Predict and display
# ---------------------------------------------------------------
if predict_button:
    input_df = build_feature_row(age, sex, bmi, children, smoker, region, model_columns)

    # Model was trained on log(charges) — convert the prediction back to real dollars
    log_prediction = model.predict(input_df)[0]
    predicted_charge = np.exp(log_prediction)

    st.subheader("Estimated Annual Charge")
    st.metric(label="Predicted Cost", value=f"${predicted_charge:,.2f}")

    if smoker == "Yes":
        st.warning(
            "Smoking status is the single biggest driver of cost in our model. "
            "Non-smoking status typically corresponds to a substantially lower estimate."
        )

    with st.expander("See the exact inputs used for this prediction"):
        st.dataframe(input_df)

st.divider()
st.caption(
    "Model: Random Forest Regressor, trained on the Kaggle Medical Cost Personal Dataset. "
    "This is an educational capstone project, not a real insurance quote."
)
