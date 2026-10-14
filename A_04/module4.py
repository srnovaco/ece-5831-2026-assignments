import numpy as np
from multilayer_perceptron import MultilayerPerceptron as mp

print("Testing Multilayer Perceptron implementation...")

# MLP with 3 input neurons, 5 hidden simoid neurons, 5 hidden sigmoid neurons, 2 hidden sigmoid neurons, and 2 relu output neurons
mlp = mp()
mlp.add_layer(weights=[[0.2, 0.4, 0.6], [0.1, 0.3, 0.5], [0.7, 0.9, 0.8], [0.5, 0.2, 0.1], [0.3, 0.6, 0.4]],
              biases=[0.1, 0.2, 0.3, 0.4, 0.5],
              activation_function=mlp.sigmoid)
mlp.add_layer(weights=[[0.5, 0.2, 0.1, 0.4, 0.3], [0.6, 0.9, 0.8, 0.7, 0.5], [0.3, 0.6, 0.4, 0.2, 0.1], [0.7, 0.5, 0.2, 0.1, 0.3], [0.4, 0.6, 0.8, 0.9, 0.7]],
              biases=[0.1, 0.2, 0.3, 0.4, 0.5],
              activation_function=mlp.sigmoid)
mlp.add_layer(weights=[[0.3, 0.6, 0.4, 0.2, 0.1], [0.7, 0.5, 0.2, 0.1, 0.3]],
              biases=[0.1, 0.2],
              activation_function=mlp.sigmoid)
mlp.add_layer(weights=[[0.5, 0.2], [0.6, 0.9]],
              biases=[0.1, 0.2],
              activation_function=mlp.relu)

# Test the forward pass with a sample input
input_data = np.array([0.5, 0.1, 0.9])
output = mlp.forward(input_data)
print("Output of the MLP for input {}: {}".format(input_data, output))

print("\n--- Hidden Layer Outputs ---")
for i, layer in enumerate(mlp.network):
    print(f"Layer {i+1} output: {layer.get_output()}")