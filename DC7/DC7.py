import numpy as np

# Generate dummy data
def generate_dummy_data(samples=100, features=10):
    X = np.random.rand(samples, features)
    y = np.random.randint(0, 2, size=samples)  # 0 = healthy, 1 = damaged
    return X, y

# AIRS Algorithm
class AIRS:
    def __init__(self, num_detectors=10, mutation_rate=0.1):
        self.num_detectors = num_detectors
        self.mutation_rate = mutation_rate

    def train(self, X, y):
        # Randomly select detectors
        indices = np.random.choice(len(X), self.num_detectors, replace=False)
        self.detectors = X[indices]
        self.detector_labels = y[indices]

        # Mutation (simulate learning)
        for i in range(len(self.detectors)):
            if np.random.rand() < self.mutation_rate:
                self.detectors[i] += np.random.normal(0, 0.1, size=self.detectors[i].shape)

    def predict(self, X):
        predictions = []
        for sample in X:
            distances = np.linalg.norm(self.detectors - sample, axis=1)
            idx = np.argmin(distances)
            predictions.append(self.detector_labels[idx])  # correct label
        return np.array(predictions)

# Data
X, y = generate_dummy_data()

# Train-test split
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Train model
model = AIRS(num_detectors=10, mutation_rate=0.1)
model.train(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = np.mean(y_pred == y_test)

print("Accuracy:", accuracy)
