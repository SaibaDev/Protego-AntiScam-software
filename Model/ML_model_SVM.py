from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Assuming 'label' is the column representing the target variable
X = final_dataset[feature_columns]
y = final_dataset['label']  # Replace 'label' with your actual target variable name

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


