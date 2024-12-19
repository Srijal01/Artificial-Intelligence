import numpy as np
def unit_step(x):
    return np.where(x > 0, 1, 0)
class Perceptron:
    def __init__(self, lr, itrn=100):
        self.lr = lr               # Learning rate
        self.itrn = itrn           # Number of iterations
        self.activation = unit_step # Activation function
        self.weights = None        # Weights initialization
        self.bias = 0              # Bias initialization
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features) # Initialize weights
        # Learn weights
        for _ in range(self.itrn):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation(linear_output)
                # Weight update
                error = self.lr * (y[idx] - y_predicted)
                self.weights += error * x_i
                self.bias += error
    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation(linear_output)
        return y_predicted
# Example usage
if __name__ == "__main__":
    # Example dataset (AND logic gate)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])  # Labels for the AND gate
    # Create and train the perceptron
    perceptron = Perceptron(lr=0.1, itrn=10)
    perceptron.fit(X, y)
    # Make predictions
    predictions = perceptron.predict(X)
    print("Predictions:", predictions)