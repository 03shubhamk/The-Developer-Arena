import joblib
def predict(model_path,X):
    return joblib.load(model_path).predict(X)
