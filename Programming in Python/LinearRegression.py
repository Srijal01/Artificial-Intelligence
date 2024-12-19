import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing

# 1. Load the California Housing dataset
california = fetch_california_housing()

# Create a DataFrame
df = pd.DataFrame(california.data, columns=california.feature_names)
df['Price'] = california.target  # Add the target variable (Price)

# 2. Split the dataset into features (X) and target (y)
X = df.drop('Price', axis=1)  # Features
y = df['Price']  # Target variable

# 3. Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Create a Linear Regression model
model = LinearRegression()

# 5. Train the model
model.fit(X_train, y_train)

# 6. Make predictions on the test set
y_pred = model.predict(X_test)

# 7. Evaluate the model's performance
# Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# R-squared score
r2 = r2_score(y_test, y_pred)
print(f"R-squared score: {r2}")

# 8. Visualize the predicted vs actual prices (only for one feature here for simplicity)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()

# 9. Print the coefficients (weights)
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
