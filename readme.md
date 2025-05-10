# 📊 Customer Churn Prediction

## 🧠 Problem Statement

Customer churn is a major concern for subscription-based businesses. Predicting which customers are likely to leave enables companies to take proactive measures to retain them. This project aims to build a machine learning model that can predict customer churn based on various demographic and service-related features.

## 📂 Dataset

The dataset contains customer information such as:

- Demographics (gender, age, senior citizen status)
- Services (internet, phone, contract type)
- Account information (tenure, monthly charges, total charges)
- Target: `Churn` (Yes/No)

## ⚙️ Workflow Summary

1. **Exploratory Data Analysis (EDA)**:  
   - Checked for missing values and outliers  
   - Analyzed churn distribution and feature relationships

2. **Data Preprocessing**:  
   - Categorical encoding (Label Encoding / One-Hot Encoding)  
   - Feature scaling  
   - SMOTE applied to balance the dataset

3. **Modeling**:  
   - Used classification models to predict churn  
   - Evaluated using metrics: accuracy, precision, recall, F1-score

4. **Model Evaluation**:  
   - Precision-Recall Curve  
   - Feature Importance plot for interpretability

## 📈 Key Insights

- SMOTE improved performance on the minority class (churned customers)
- Contract type and tenure are strong predictors of churn
- Precision-Recall curve shows trade-offs useful for real-world deployment

## ✅ Conclusion

A well-performing and interpretable churn prediction model was developed, which can help businesses reduce churn through targeted retention strategies.

## 🚀 Future Improvements

- To add more models like XGBoost or Logistic Regression for comparison
- Hyperparameter tuning for model optimization
- To use SHAP for advanced explainability
- Deploying the model using Streamlit or Flask
