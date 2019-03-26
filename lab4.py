import numpy as np

Function = lambda net: (1-np.exp(-net))/(1+np.exp(-net))

Deriv_func = lambda net: (1 - Function(net)**2)/2

class Neuron:
    def __init__(self, number_w, nu):
        self.w = np.zeros(number_w)
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
        self.era = 0
        self.x = x
        self.t = t
        self.J = J
        self.eps = eps
        self.hide_level = [Neuron(len(x), nu) for _ in range(J)]
        self.enter_level = [Neuron(J+1, nu) for _ in range(len(t))]

    def Era(self):
        hide_out = [1] + [hide_neuron.Get_out(self.x)
                        for hide_neuron 
                        in self.hide_level]
        enter_out = [enter_neuron.Get_out(hide_out)
                        for enter_neuron 
                        in self.enter_level]
        primary_sigma = [self.t[i] - enter_out[i]
                        for i in range(len(self.t))]
        enter_mistake = [enter_neuron.Get_mistake(primary_sigma[i])
                        for i, enter_neuron
                        in enumerate(self.enter_level)]
        enter_mistake = [sum(line[i] for line in enter_mistake) for i in range(self.J)]
        _ = [hide_neuron.Get_mistake(enter_mistake[i])
                        for i, hide_neuron
                        in enumerate(self.hide_level)]
        _ = [hide_neuron.Correct_w(self.x)
                        for hide_neuron
                        in self.hide_level]
        _ = [enter_neuron.Correct_w(hide_out)
                        for enter_neuron
                        in self.enter_level]
        squared_mistake = sum(i**2 for i in primary_sigma)**0.5
        print(f"Era: {self.era}   Vector: {', '.join(str(np.around(i, 3)) for i in enter_out)}    Error: {np.around(squared_mistake, 4)}")
        self.era+=1
        return squared_mistake

    def Work(self):
        while self.Era() > self.eps:
            pass


if __name__ == "__main__":
    Nn = Neuron_Net([1,4], 2, [-0.2], 1, 0.001)
    Nn.Work()
