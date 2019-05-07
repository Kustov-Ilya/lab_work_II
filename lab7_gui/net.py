import numpy as np


class HopfieldNet:
    def __init__(self, height, widht):
        self.drawsteps = False
        self.shapes = []
        self.neurons = height*widht
        self.height = height
        self.widht = widht
        self.W = np.array([np.zeros(self.neurons) for _ in range(self.neurons)])

    def teach(self, shape):
        self.shapes.append(shape)
        self.W += np.array([[shape[i] * shape[j] if j != i else 0
                            for j in range(self.neurons)]
                            for i in range(self.neurons)])

    def recognize(self, shape):
        def sign(net):
            if net < 0:
                return -1
            elif net > 0:
                return 1
            else:
                return 0
        for i in range(self.neurons):
            net = 0
            net = sum([self.W[i][j]*shape[j] for j in range(self.neurons)])
            y = sign(net)
            if y != shape[i] and y != 0:
                print(f'Neuron {i}: {shape[i]} -> {y}')
                shape[i] = y
        return ('Success' if shape in self.shapes else 'Failed', shape)

    def clear(self):
        self.shapes.clear()
        self.W = np.array([np.zeros(self.neurons) for _ in range(self.neurons)])
