import numpy as np
import os
import matplotlib.pyplot as plt 

Function = lambda net: (1-np.exp(-net))/(1+np.exp(-net))

Deriv_func = lambda net: (1 - Function(net)**2)/2


class Neuron:
    def __init__(self, number_w, nu, hide):
        self.w = np.ones(number_w) #if hide==True else np.zeros(number_w)
        self.nu = nu
        self.net = 0
        self.sigma = 0

    def Get_out(self, x):
        self.net = np.dot(self.w, x)
        return Function(self.net)

    def Get_mistake(self, sigma):
        self.sigma = Deriv_func(self.net)*sigma
        return [self.sigma*wi for wi in self.w[1:]]

    def Correct_w(self, x):
        self.w+= [self.nu*self.sigma*xi for xi in x]
        self.net, self.sigma = 0, 0

class Neuron_Net:
    def __init__(self, x, J, t, nu, eps):
        self.era = -1
        self.x = x
        self.t = t
        self.J = J
        self.eps = eps
        self.hide_level = [Neuron(len(x), nu, True) for _ in range(J)]
        self.output_level = [Neuron(J+1, nu, False) for _ in range(len(t))]
        self.mistakes =[]

    def Era(self):
        self.era+=1
        hide_out = [1] + [hide_neuron.Get_out(self.x)
                        for hide_neuron
                        in self.hide_level]
        output_out = [output_neuron.Get_out(hide_out)
                        for output_neuron
                        in self.output_level]
        primary_sigma = [self.t[i] - output_out[i]
                        for i in range(len(self.t))]
        squared_mistake = sum(i**2 for i in primary_sigma)**0.5
        self.mistakes.append(squared_mistake)
        print(f"Era: {self.era}   y: {', '.join(str(np.around(i, 3)) for i in output_out)}    Mistake: {np.around(squared_mistake, 4)}", end = ' ')
        print("Hide", end = ' ')
        for i, neuron in enumerate(self.hide_level):
            print(f"{i+1}. {np.around(neuron.w, 3)}", end = ' ')
        print("Output", end = ' ')
        for i, neuron in enumerate(self.output_level):
            print(f"{i+1}. {np.around(neuron.w, 3)}", end = ' ')
            print('\n')
        output_mistake = [output_neuron.Get_mistake(primary_sigma[i])
                        for i, output_neuron
                        in enumerate(self.output_level)]
        output_mistake = [sum(line[i] for line in output_mistake) for i in range(self.J)]

        _ = [hide_neuron.Get_mistake(output_mistake[i])
                        for i, hide_neuron
                        in enumerate(self.hide_level)]
        _ = [hide_neuron.Correct_w(self.x)
                        for hide_neuron
                        in self.hide_level]
        _ = [output_neuron.Correct_w(hide_out)
                        for output_neuron
                        in self.output_level]
        return squared_mistake

    def graf(self):
        x = range(self.era+1)
        plt.plot(x, self.mistakes)
        plt.xlabel('Eras')
        plt.ylabel('Errors')
        plt.show()

    def Work(self):
        while self.Era() > self.eps:
            pass
        self.graf()


if __name__ == "__main__":
    Nn = Neuron_Net([1, 4], 2, [-0.2], 0.3, 0.001)
    Nn.Work()
    os.system("pause")

