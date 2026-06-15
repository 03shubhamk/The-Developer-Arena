# Feature Engineering Documentation

## Objective
Improve model performance by creating meaningful features.

## Suggested Engineered Features

### 1. Customer Lifetime Value
tenure * MonthlyCharges

### 2. Average Monthly Spend
TotalCharges / tenure

### 3. Contract Risk Score
Map contract types to numerical risk values.

### 4. Service Count
Count active subscribed services.

### 5. Payment Efficiency
Automatic payment = 1, Manual payment = 0

### 6. Internet Dependency Score
Number of internet-related services used.

## Feature Selection Techniques
- Correlation Analysis
- Mutual Information
- Random Forest Feature Importance
- Recursive Feature Elimination (RFE)

## Expected Outcome
More informative features and improved churn prediction performance.
