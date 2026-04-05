# 🚚 Segment Delivery Time Prediction (ML + Streamlit)

🚀 **Live Streamlit App:**  
👉 https://segment-delivery-time-prediction-marxks6dvhw22ky5np5bb5.streamlit.app

> **End-to-end Machine Learning project to predict segment-level delivery time using real-world logistics data, advanced feature engineering, and CatBoost regression, deployed via a Streamlit web application.**

---


## 📌 Problem Statement

Accurate delivery time estimation is critical in logistics and supply chain operations.  
This project focuses on predicting **segment-level delivery time** (not final ETA) using historical trip, route, and temporal data.

The objective is to:
- Capture **route- and segment-level patterns**
- Handle **high-cardinality categorical features**
- Build a **robust, non-overfitted regression model**
- Provide **real-time predictions** via a web interface

---

## 🧠 Solution Overview

- Performed **extensive feature engineering** on:
  - Trip timestamps
  - Route and segment attributes
  - Distance–time interactions
- Applied **log transformation on the target variable** to stabilize variance and improve MAE
- Compared multiple regression models:
  - Linear Regression
  - Random Forest
  - **CatBoost (final selected model)**
- Deployed the trained model using **Streamlit** for interactive inference

---

## 🛠️ Tech Stack

- **Programming:** Python  
- **Data Processing:** Pandas, NumPy  
- **Modeling:** Scikit-learn, CatBoost  
- **Visualization:** Matplotlib, Seaborn  
- **Deployment:** Streamlit  
- **Version Control:** Git, GitHub  

---

## 📊 Model Performance (Validation)

| Model              | MAE ↓ | RMSE ↓ |
|-------------------|------|--------|
| Linear Regression | High | High   |
| Random Forest     | Moderate | Moderate |
| **CatBoost (Final)** | **~29** | **~58** |

> ✅ CatBoost was selected due to superior generalization and strong handling of categorical features.

---

## 🔍 Feature Engineering Highlights

- Temporal features:
  - Hour of day
  - Day of week
  - Weekend indicator
- Route & distance interactions:
  - `hour × distance`
  - `hour × OSRM time`
- Segment-level aggregation features
- Strict preprocessing to ensure **training–inference schema consistency**

---

## 🧪 Dataset

📎 **Dataset link (add here):**  
👉 TRAINING DATA :- https://drive.google.com/file/d/1QtYlVA4QOBkfmvKiPrxstx2Z1Y73bVP3/view?usp=sharing
    TEST DATA :- https://drive.google.com/file/d/1s_OtoWwvTdsktEyeJ4TPcONCRwaQLqzm/view?usp=sharing

> ⚠️ Datasets are **not included** in this repository due to size and privacy constraints.  
Please download the dataset separately and place it as instructed in the notebook.

---

## 🚀 Running the Project Locally

1️⃣ Clone the repository

git clone https://github.com/shvhjSB/segment-delivery-time-prediction.git
cd segment-delivery-time-prediction

2️⃣ Create a virtual environment
python -m venv myvenv
myvenv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit app
streamlit run app.py


## 📈 Future Improvements

- K-Fold cross-validation for stronger generalization  
- Model explainability using SHAP  
- Final ETA prediction by aggregating multiple segments  
- Cloud deployment

---

## 🎯 Key Learnings

- Importance of maintaining **feature schema consistency** between training and inference in ML deployment  
- Effective handling of **high-cardinality categorical features** using CatBoost  
- Preventing model overfitting through:
  - Log-transformed target variable  
  - Proper validation strategy  
- Designing a complete **end-to-end ML system** (training → inference → UI)
