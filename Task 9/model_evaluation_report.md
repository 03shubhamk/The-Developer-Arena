# House Price Prediction - Model Evaluation Report

## Project Overview

The objective of this project is to develop a machine learning model that predicts house prices based on various property features such as area, number of bedrooms, bathrooms, location, and property age. Accurate house price prediction helps buyers, sellers, and real estate businesses make informed decisions.

## Dataset Description

The dataset contains information about residential properties and their corresponding prices.

### Features Used

* Area (Square Feet)
* Number of Bedrooms
* Number of Bathrooms
* Property Age
* Location
* House Price (Target Variable)

### Dataset Preparation

* Loaded the dataset using Pandas.
* Checked for missing values and handled them appropriately.
* Converted categorical variables into numerical format using One-Hot Encoding.
* Split the dataset into training and testing sets using an 80:20 ratio.

## Methodology

### Step 1: Data Exploration

* Analyzed dataset structure and feature distributions.
* Identified correlations between variables.
* Visualized important relationships using graphs.

### Step 2: Data Preprocessing

* Removed or handled missing values.
* Encoded categorical features.
* Selected relevant features for prediction.

### Step 3: Model Development

A Linear Regression model was implemented using Scikit-Learn.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

### Step 4: Model Evaluation

The model was evaluated using the following metrics:

#### Mean Absolute Error (MAE)

Measures the average prediction error.

#### Mean Squared Error (MSE)

Measures the average squared prediction error.

#### R² Score

Indicates how well the model explains the variance in house prices.

## Results

| Metric   | Value                |
| -------- | -------------------- |
| MAE      | 2,188,736.34         |
| MSE      | 8,454,330,868,276.11 |
| R² Score | 0.9406               |

## Interpretation of Results

### MAE

The model's average prediction error is approximately ₹21.9 lakhs.

### MSE

Large errors are penalized more heavily due to squaring.

### R² Score

An R² score of 0.9406 indicates that the model explains approximately 94% of the variation in house prices.

## Feature Importance Analysis

Based on correlation and model coefficients, the most influential features are:

1. Area
2. Location
3. Number of Bedrooms
4. Number of Bathrooms

These variables significantly affect the final house price prediction.

## Visualization

A scatter plot comparing actual house prices and predicted house prices was generated.

### Observation

* Most predicted values closely follow actual values.
* The model demonstrates strong predictive performance.
* A few outliers are present but do not significantly affect overall accuracy.

## Challenges Faced

* Handling categorical variables such as location.
* Managing missing values.
* Ensuring proper train-test splitting to avoid data leakage.

## Conclusion

The Linear Regression model successfully predicts house prices with high accuracy. The achieved R² score of 0.9406 indicates strong model performance. Area and location were identified as the most important factors influencing house prices.

## Future Improvements

* Implement Decision Tree Regression.
* Implement Random Forest Regression.
* Perform Hyperparameter Tuning.
* Add more property features.
* Use Cross-Validation for improved reliability.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Jupyter Notebook

## Project Structure

```text
House-Price-Prediction/
│
├── house_price_prediction.ipynb
├── house_data.csv
├── model_evaluation_report.md
├── requirements.txt
├── predictions_vs_actual.png
└── README.md
```

## References

* Scikit-Learn Documentation
* Pandas Documentation
* Machine Learning by Andrew Ng
* Python Official Documentation
