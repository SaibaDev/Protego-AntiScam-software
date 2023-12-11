import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier
import joblib
import logging

logging.basicConfig(level=logging.DEBUG)


file_path = 'Extracted_features\parsed_Fextracted1.csv'  
data = pd.read_csv(file_path)


features = data.drop(['url', 'label'], axis=1)  
labels = data['label']
logging.debug("#Extract features and labels")


X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
logging.debug("# Split the data into training and testing sets")


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
logging.debug("# Standardize the features (optional but often improves performance)")


rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
logging.debug(" Train Random Forest Classifier")


svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)
logging.debug("# Train Support Vector Machine (SVM) Classifier")


voting_model = VotingClassifier(estimators=[('rf', rf_model), ('svm', svm_model)], voting='hard')
voting_model.fit(X_train, y_train)


voting_predictions = voting_model.predict(X_test)
logging.debug("Make predictions on the test set")


print("Voting Model Accuracy:", accuracy_score(y_test, voting_predictions))
print("Voting Model Classification Report:\n", classification_report(y_test, voting_predictions))
logging.debug("Evaluate the Voting Model")


joblib.dump(voting_model, 'voting_model.joblib')
logging.debug("# Save the trained models to files")
