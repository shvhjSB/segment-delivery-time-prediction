# 🕒 Time Predictor – ML Model for Estimating Product Delivery Time

A machine learning project that predicts the **estimated delivery time** of a product using structured historical data. The model leverages feature engineering, data normalization, and advanced regression algorithms to deliver high accuracy.

---

## 📌 Key Highlights

- ✅ **Complete ML pipeline** from preprocessing to prediction.
- 🧹 **Feature extraction and normalization** using `StandardScaler`.
- 🤖 **Evaluated multiple models**:
  - XGBoost 
  - CatBoost(best performing)
  - Random Forest
- 🧠 Final model: **CatBoost Regressor**

---
# Datasets:-
TRAINING DATASET = https://drive.google.com/file/d/1rYs3KZbEviiaX5GjH-0NSQW-MNq2Jg3m/view?usp=
TEST DATASET = https://drive.google.com/file/d/15NhhxXxS_Wz8VPBuc5I3yZ7-Twvmrx53/view?usp=drive_link

---

## 🧰 Tools & Technologies

| Category       | Tools / Libraries                                |
|----------------|--------------------------------------------------|
| Language       | Python                                           |
| Notebook       | Google Colab                                     |
| ML Libraries   | Scikit-learn, XGBoost, CatBoost                   |
| Data Handling  | Pandas, NumPy                                     |
| Visualization  | Matplotlib, Seaborn                               |

---

## 🧪 Workflow

1. **Data Loading**  
   Load dataset from CSV.

2. **Feature Engineering**  
   - Extract features from raw columns  
   - Encode categorical data  
   - Handle missing values

3. **Normalization**  
   Applied `StandardScaler` for consistent scaling.

4. **Model Training & Evaluation**  
   - Used Train/Test split  
   - Trained XGBoost, CatBoost, and Random Forest  
   - Selected **CatBoost** based on RMSE and R²

5. **Prediction**  
   Predict delivery times on new input data.

---

## 📈 Model Performance

| Metric         | Value (Example)  |
|----------------|------------------|
| R² Score       | 0.9985            |
| RMSE           | 26.62          |
| MAE            | 18.26            |

> *Replace with your actual evaluation metrics after running the notebook.*

---

## 🚀 Use Cases

- Delivery & Logistics ETA Forecasting  
- Supply Chain Optimization  
- E-commerce Tracking Systems  
- Timeline Estimation for Products or Projects

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute.

---
