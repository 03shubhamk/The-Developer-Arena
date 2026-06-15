# Customer Churn Prediction - Preprocessing Report

## Project Objective
Predict customer churn using machine learning after applying data preprocessing and feature engineering.

## Dataset Overview
- Rows: 500
- Columns: 9

## Preprocessing Steps
1. Load dataset and inspect data types.
2. Handle missing values.
3. Encode categorical variables using:
   - Label Encoding
   - One-Hot Encoding
   - Ordinal Encoding (where applicable)
4. Apply feature scaling:
   - StandardScaler
   - MinMaxScaler
5. Detect outliers using:
   - IQR Method
   - Z-Score Method
6. Perform feature selection using correlation and feature importance.
7. Build a preprocessing pipeline using scikit-learn.

## Validation
- Train/Test Split
- Cross Validation
- Accuracy, Precision, Recall and F1 Score

## Conclusion
A complete preprocessing workflow was implemented before model training.
