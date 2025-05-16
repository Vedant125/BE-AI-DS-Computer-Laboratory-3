'''Practicle 7 : To apply the artificial immune pattern recognition to perform a 
task of structure damage Classification.'''


import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Simulate Clonal Selection Algorithm
def clonal_selection_algorithm(X_train, y_train, X_test, num_clones=10, mutation_rate=0.1):
    num_features = X_train.shape[1]
    memory_cells = []

    # Memory cell creation
    for i in range(len(X_train)):
        memory_cells.append((X_train[i], y_train[i]))

    predictions = []
    for test_sample in X_test:
        best_match = None
        best_affinity = float('inf')

        # Find best match (affinity based on distance)
        for mem in memory_cells:
            distance = np.linalg.norm(test_sample - mem[0])
            if distance < best_affinity:
                best_affinity = distance
                best_match = mem

        # Clone best match and mutate
        clones = [best_match[0] + np.random.normal(0, mutation_rate, size=num_features) for _ in range(num_clones)]
        clone_affinities = [np.linalg.norm(test_sample - clone) for clone in clones]
        best_clone = clones[np.argmin(clone_affinities)]

        # Assign class of the original best match
        predictions.append(best_match[1])
    return predictions

# Generate synthetic dataset for structure damage (0: Undamaged, 1: Damaged)
X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Apply the AIS-based classifier
y_pred = clonal_selection_algorithm(X_train, y_train, X_test, num_clones=20, mutation_rate=0.05)

# Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
print("Structure Damage Classification Accuracy (AIS):", accuracy)
