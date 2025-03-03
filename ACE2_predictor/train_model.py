import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pickle
from Bio import SeqIO

# Load extracted features
with open("onehot_features.pkl", "rb") as f:
    X = pickle.load(f)  # Shape: (528, 7093, 20)

# Dummy labels (Replace with real labels if available)
y = np.random.randint(0, 2, size=(X.shape[0],))  # Binary labels (0 or 1)

# Define CNN Model
model = keras.Sequential([
    layers.Conv1D(filters=64, kernel_size=3, activation="relu", input_shape=(X.shape[1], X.shape[2])),
    layers.MaxPooling1D(pool_size=2),
    layers.Conv1D(filters=128, kernel_size=3, activation="relu"),
    layers.MaxPooling1D(pool_size=2),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(1, activation="sigmoid")  # Binary classification output
])

# Compile model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train model
model.fit(X, y, epochs=10, batch_size=16, validation_split=0.2)

# Save model
model.save("ACE2_mutation_predictor.h5")
print("✅ Model training complete. Saved as ACE2_mutation_predictor.h5")
