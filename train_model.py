import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib


data = pd.read_csv('/content/drive/MyDrive/rdataset.csv')  

X = data.drop('Malware', axis=1)  
y = data['Malware']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


clf = RandomForestClassifier(n_estimators=100, random_state=42)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

joblib.dump(clf, 'fake_app_detector_model.pkl')

model = joblib.load('fake_app_detector_model.pkl')

