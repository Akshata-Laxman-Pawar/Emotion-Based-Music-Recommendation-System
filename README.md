# Emotion-Based Music Recommendation System
# Overview
This project aims to recommend music based on the user's emotional state detected through real-time video input. By leveraging deep learning techniques, the system can classify emotions and suggest suitable music tracks.

# Model Architecture
Input Layer: Takes an input of shape (X.shape[1]), where X represents the feature set.
Hidden Layers:
First hidden layer with 512 units and ReLU activation.
Second hidden layer with 256 units and ReLU activation.
Output Layer: Dense layer with softmax activation, where the number of units corresponds to the number of emotion classes.

# Training Details
Loss Function: Categorical crossentropy.
Optimizer: RMSprop.
Metrics: Accuracy.
Epochs: Trained for 50 epochs.

# Implementation Details
The project uses Keras and TensorFlow for building and training the neural network.
OpenCV and MediaPipe are utilized for capturing and processing real-time video input to detect facial landmarks and hand positions.
NumPy is used for data manipulation and preprocessing.
Usage
Data Collection: Collect emotion-labeled audio data and preprocess it for training.
Model Training: Run data_training.py to train the model with the preprocessed data.
Real-Time Emotion Detection: Use inference.py to start the real-time emotion detection system.

Requirements
Python 3.x
TensorFlow
Keras
OpenCV
MediaPipe
NumPy
