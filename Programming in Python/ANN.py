import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
# 1. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# 2. One-hot encode the target variable (y) using Keras to_categorical
y = to_categorical(y, num_classes=3)
# 3. Split the data into training and test sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 4. Feature scaling: Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# 5. Build the ANN model
model = Sequential()
# Input layer (with input dimension equal to the number of features, i.e., 4)
model.add(Dense(units=8, activation='relu', input_dim=X_train.shape[1]))
# Hidden layer with 8 neurons
model.add(Dense(units=8, activation='relu'))
# Output layer with 3 units (for 3 classes) and softmax activation
model.add(Dense(units=3, activation='softmax'))
# 6. Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# 7. Train the model for 10 epochs
history = model.fit(X_train, y_train, epochs=10, batch_size=10, validation_data=(X_test, y_test))
# 8. Evaluate the model on test data
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Test accuracy: {test_acc}")
# 9. Visualize the training history (optional)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Test Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()