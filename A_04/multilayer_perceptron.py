import numpy as np

class MultilayerPerceptron:
    def __init__(self):
        self.network = []

    def __str__(self):
        return "Multilayer Perceptron with {} layers".format(len(self.network))

    def __size__(self):
        return len(self.network)

    class Layer:
        def __init__(self, weights, biases, activation_function):
            self.weights = np.array(weights)
            self.biases = np.array(biases)
            self.activation_function = activation_function
            self.output = None  # Initialize output to None

        def __str__(self):
            return "Layer with weights: {}, biases: {}, activation_function: {}".format(
                self.weights, self.biases, self.activation_function.__name__)

        def get_weights(self):
            return self.weights

        def get_biases(self):
            return self.biases

        def get_activation_function(self):
            return self.activation_function

        def get_output(self):
            return self.output

    def add_layer(self, weights, biases, activation_function):
        layer = self.Layer(weights, biases, activation_function)
        self.network.append(layer)

    def set_layer(self, index, layer):
        if index < len(self.network):
            self.network[index] = layer
        else:
            raise IndexError("Layer index out of range.")

    def get_layer(self, index):
        if index < len(self.network):
            return self.network[index]
        else:
            raise IndexError("Layer index out of range.")

    def remove_layer(self, index):
        if index < len(self.network):
            del self.network[index]
        else:
            raise IndexError("Layer index out of range.")

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def forward(self, input_data):
        output = input_data
        for layer in self.network:
            z = np.dot(layer.get_weights(), output) + layer.get_biases()
            output = layer.get_activation_function()(z)
            layer.output = output
        return output