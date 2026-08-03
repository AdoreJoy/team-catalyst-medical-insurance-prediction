# Medical Insurance Cost Prediction

**Team Catalyst — Tech4Africans Data Science Bootcamp, Cohort 7**
Machine learning capstone project predicting individual healthcare insurance costs using demographic and lifestyle data.

---

##  Live Demo

Try the prediction app here: **[Medical Insurance Cost Predictor](https://team-catalyst-medical-insurance-prediction-mqusabajuxzru8hy5xt.streamlit.app/)**

Enter age, BMI, smoker status, and other details to get an instant estimated insurance cost, powered by our trained Random Forest model (R² = 0.876).

---

## Problem Statement

Healthcare expenses vary significantly among individuals due to differences in age, lifestyle, medical history, and demographic factors. Insurance providers need accurate cost estimation models to improve pricing strategies, risk assessment, and financial planning.

This project builds a regression model that predicts expected annual medical insurance charges for a customer based on their personal and health-related information, and identifies which factors most strongly influence cost — with the goal of supporting data-driven pricing and underwriting decisions.

---

## Dataset

Source: [Kaggle — Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance/data)

- **Size:** 1,338 rows
- **Features:** `age`, `sex`, `bmi`, `children`, `smoker`, `region`
- **Target:** `charges` (annual medical insurance cost, in USD)

---

## Key Findings

- **Smoking status is the dominant cost driver.** Smokers pay roughly 3–4x more on average than non-smokers — by far the strongest single predictor in the dataset.
- **BMI matters most in combination with smoking.** Non-smokers show a fairly flat relationship between BMI and charges, but smokers with a BMI above ~30 (obesity threshold) see a sharp additional cost increase. This BMI × smoker interaction was engineered as an explicit feature.
- **Age contributes a steady, predictable increase** in cost for both smokers and non-smokers, though the increase is steeper for smokers.
- **Region, sex, and number of children have minimal impact** on cost — worth noting for simplifying real-world pricing models.

---

## Model Performance

Two regression models were built and compared:

| Model | R² | RMSE | MAE |
|---|---|---|---|
| Linear Regression | 0.814 | $5,378.57 | $2,600.77 |
| **Random Forest (selected)** | **0.876** | **$4,395.29** | **$2,083.63** |

**Random Forest was selected for deployment** — it outperforms Linear Regression on every metric and requires no feature scaling, simplifying the deployment pipeline. Linear Regression remains useful as an interpretability check, since its coefficients are directly human-readable.

---

## Repository Structure

```
team-catalyst-medical-insurance-prediction/
├── README.md
├── requirements.txt
├── data/
│   └── raw/
│       └── insurance.csv
├── notebooks/
│   └── Capstone_Insurance.ipynb
├── reports/
│   ├── figures/
│   ├── coefficients.csv
│   └── feature_importance.csv
├── app/
│   ├── app.py
│   ├── model.pkl
│   └── model_columns.pkl
├── presentation/
└── .github/workflows/
    └── run-notebooks.yml
```

---

## How to Reproduce

Clone the repo and install dependencies:

```bash
git clone https://github.com/AdoreJoy/team-catalyst-medical-insurance-prediction.git
cd team-catalyst-medical-insurance-prediction
pip install -r requirements.txt
```

- The full analysis (EDA, feature engineering, modeling, evaluation) is in `notebooks/Capstone_Insurance.ipynb`
- The deployed prediction app is in `app/app.py` — run locally with:
  ```bash
  cd app
  streamlit run app.py
  ```

---

## Future Improvements

While this project provides a reliable prediction model for healthcare insurance costs, there are several opportunities to enhance its performance and real-world applicability:

- **Collect richer healthcare data:** Include additional features such as medical history, chronic diseases, physical activity, alcohol consumption, occupation, and income to improve prediction accuracy.

- **Hyperparameter tuning:** Optimize the Random Forest model using techniques such as Grid Search or Randomized Search to further improve performance.

- **Experiment with advanced models:** Compare the current model with algorithms such as XGBoost, LightGBM, CatBoost, or Gradient Boosting Regressor.

- **Explain model predictions:** Integrate Explainable AI (XAI) tools such as SHAP or LIME to show users how each feature influences an individual prediction.

- **Enhance the Streamlit application:** Add data visualizations, confidence intervals, input validation, downloadable prediction reports, and a more interactive user interface.

- **Cloud deployment and monitoring:** Deploy the application on cloud platforms such as AWS, Azure, or Google Cloud Platform and monitor model performance over time.

- **Continuous model retraining:** Update the model periodically with new insurance data to ensure predictions remain accurate as healthcare trends change.

- **API integration:** Develop a REST API that allows insurance companies or third-party applications to access the prediction model programmatically.

- **Model fairness assessment:** Evaluate the model for potential bias across demographic groups to support fair and ethical insurance pricing.

---

## Project Vision

This project demonstrates how machine learning can support data-driven decision-making in the healthcare insurance industry. Our long-term vision is to evolve this prototype into a scalable decision-support system that enables insurance providers to estimate medical costs more accurately, improve risk assessment, and deliver fairer, more transparent pricing for customers.

---

## Tech Stack

Python · pandas · NumPy · scikit-learn · matplotlib · seaborn · Streamlit · joblib

---

## Team Catalyst

| # | Role | Member |
|---|------|--------|
| 1 | Team Lead / Project Manager | Adorejoy |
| 2 | Data Understanding & Documentation | Sakirat |
| 3 | Data Cleaning & Preprocessing | O'Laja |
| 4 | Exploratory Data Analysis — Part 1 | O'Laja & Sakirat |
| 5 | Exploratory Data Analysis — Part 2 | Peace |
| 6 | Feature Engineering & Data Preparation | Mosope |
| 7 | Model Building | Sylvia |
| 8 | Model Evaluation | Adorejoy & Ibrahim Ajiboso |
| 9 | Documentation (GitHub README & Medium Report) | Adebiyi |
| 10 | Presentation & Slide Design | Judith Amaka & Onyekachi Ubadire |

---

## Deliverables

- ✅ GitHub Repository (this repo)
- ✅ Live prediction app — (https://team-catalyst-medical-insurance-prediction-mqusabajuxzru8hy5xt.streamlit.app/)
- 📝 Medium article —(https://medium.com/@realadorejoy/predicting-medical-insurance-costs-with-machine-learning-a-team-catalyst-capstone-project-ecb9e21d520c)
- 📊 Presentation deck — (https://docs.google.com/presentation/d/1HJDAIxplUoCYUWX43LKrJ2pfbA_BcxweNODkVXXrKA8/edit?usp=sharing)

---

*Capstone project for Tech4Africans Data Science Bootcamp, Cohort 7 — Case Study 1: Healthcare, Medical Insurance Cost Prediction.* 