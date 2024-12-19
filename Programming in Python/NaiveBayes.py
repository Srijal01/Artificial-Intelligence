import numpy as np
import pandas as pd
import zipfile
import urllib.request
import os
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Define URL and download the ZIP file
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"
zip_file_path = r'C:\Users\DELL\Downloads\smsspamcollection.zip'

# Download the file
urllib.request.urlretrieve(url, zip_file_path)

# 2. Extract the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(r'C:\Users\DELL\Downloads')  # Specify extraction path

# Check if file exists
file_path = r'C:\Users\DELL\Downloads\SMSSpamCollection'
if os.path.exists(file_path):
    # 3. Load the dataset from the extracted file
    df = pd.read_csv(file_path, sep='\t', header=None, names=['label', 'message'])
else:
    print("File not found!")
    exit()

# 4. Preprocess the data: Convert labels into binary values (1 for spam, 0 for ham)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 5. Split the dataset into features (X) and target (y)
X = df['message']  # Feature: text messages
y = df['label']    # Target: 0 for ham, 1 for spam

# 6. Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Convert the text data to a bag-of-words model using CountVectorizer
vectorizer = CountVectorizer(stop_words='english')

# Fit the vectorizer to the training data and transform both training and testing data
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# 8. Initialize and train the Naive Bayes classifier (MultinomialNB for text classification)
nb = MultinomialNB()

# Train the Naive Bayes classifier
nb.fit(X_train_vectorized, y_train)

# 9. Make predictions on the test set
y_pred = nb.predict(X_test_vectorized)

# 10. Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
