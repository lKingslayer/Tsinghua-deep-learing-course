""" Sigmoid Layer """

import numpy as np


class SigmoidLayer(object):

    def __init__(self):
        """
        Applies the element-wise function: f(x) = 1/(1+exp(-x))
        """

        self.trainable = False

    def forward(self, Input):

        ############################################################################
        # TODO: Put your code here
        # Apply Sigmoid activation function to Input, and return results.

        self.Input = Input
        return 1 / (1 + np.exp(-Input))
        ############################################################################



    def backward(self, delta):

        ############################################################################
        # TODO: Put your code here
        # Calculate the gradient using the later layer's local sensitivity: delta
        y = self.Input
        sigmoid = 1/(1 + np.exp(-y))
        y = sigmoid*(1-sigmoid)
        delta = np.multiply(delta, y)
        return delta
        ############################################################################

