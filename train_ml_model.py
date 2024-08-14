import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib

# Load your dataset
df = pd.read_csv('/content/drive/MyDrive/feat.csv')

# Features and target
X = df.drop('Malware', axis=1)
y = df['Malware']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred_proba = model.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test, y_pred_proba)
print("ROC AUC Score:", roc_auc)
print("Classification Report:\n", classification_report(y_test, (y_pred_proba > 0.5).astype(int)))

# Save the model using joblib
joblib.dump(model, 'fad.pkl')
print("Model saved as fad.pkl")
