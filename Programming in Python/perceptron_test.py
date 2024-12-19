import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
# Accuracy function
def accuracy(y_true, y_predicted):
    return np.sum(y_true == y_predicted) / len(y_true)
# Define dataset
X = [0.21, 0.52, 0.92, 0.36, 0.55, 0.45, 0.34, 0.67, 0.04, 0.77]
y = [0, 1, 1, 0, 1, 0, 0, 1, 1, 1]
X = np.array([[x] for x in X])  # Reshape X into a 2D array
y = np.array(y)
# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)
# Print the datasets
print("*" * 100)
print("X_test:")
print(X_test)
print("y_test:")
print(y_test)
print("X_train:")
print(X_train)
print("*" * 100)
# Initialize Perceptron model
p = Perceptron(eta0=0.01, max_iter=1000)
# Train the model
p.fit(X_train, y_train)
# Make predictions on the test set
prediction = p.predict(X_test)
# Print predictions and accuracy
print("Predictions:", prediction)
print("Accuracy:", accuracy(y_test, prediction))
# Make predictions for new data
new_data = [[0.31], [0.88]]
new_prediction = p.predict(new_data)
print("New predictions:", new_prediction)