# Simple Keras Neural Network for Binary Classification

This repository features a Python script for building and training a simple neural network using Keras. The network consists of one hidden layer with 32 neurons, employing the ReLU activation function, and an output layer with a sigmoid activation function, suitable for binary classification tasks. The model leverages the Adam optimizer and binary cross-entropy loss function, trained over 10 epochs with mini-batch sizes of 32.

## Prerequisites

- Python 3.x
- Keras
- TensorFlow

## Installation

1. Clone this repository to your local machine:


git clone https://github.com/Marqui-13/simpleNeuralNet.git


2. Navigate to the cloned directory:


cd simple-keras-network


3. Ensure you have Python installed. If not, download it from [here](https://www.python.org/downloads/).

4. Install Keras and TensorFlow:


pip install keras tensorflow


## Usage

Before running the script, make sure you have prepared your dataset, splitting it into training (`X_train`, `y_train`) and testing (`X_test`, `y_test`) sets.

Run the neural network training and evaluation script with:


python keras_binary_classification.py


The script trains the model on the provided training data and then evaluates its performance on the test data, printing out the accuracy.

## Data Preparation

Your dataset should be divided into input features (`X_train`, `X_test`) and target labels (`y_train`, `y_test`), suitable for binary classification.

## Contributing

Your contributions to enhance the script or improve the documentation are highly welcome. Please fork the repository, apply your changes, and submit a pull request for review.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The Keras team for creating a high-level neural networks API, running on top of TensorFlow.
- The TensorFlow team for developing an open-source platform for machine learning.