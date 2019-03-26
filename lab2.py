import numpy as np
import matplotlib.pyplot as plt
import math
from multiprocessing import Process, Queue

#p - окно
#eras - колво эпох
#isplot - True, если необходимо построить предсказанную функцию, False, если вернуть ошибку
def Train(p, eras, nu, isplot = True):
    array = np.linspace(-4, 4, 20)
    matrix = [[Function(array[i + j]) for j in range(p)] for i in range(20 - p)]
    w = np.zeros(p)
    for _ in range(eras):
        error = 0
        for i in range(len(matrix)):
            sigma = Function(array[p + i]) - np.dot(w,matrix[i])
            error += sigma ** 2
            w += [nu * sigma * k for k in matrix[i]]
        error = error ** 0.5
    print(f'Era:{eras} nu = {nu} p = {p}\nVector w:{np.around(w, 3)}')
    return Plot(w, p) if isplot else (w)

def Plot(w, p):
    x = np.linspace(-4, 8, 30)
    matrix = np.array([[Function(x[i + j]) for j in range(p)] for i in range(30 - p)])
    plt.plot(x, [Function(t) for t in x])
    plt.plot(x[p:], [np.dot(w, arr) for arr in matrix])
    print(f'Error: {np.around(Get_error(w, p), 4)}')
    plt.show()

def Get_error(w, p):
    x = np.linspace(-4, 8, 30)
    matrix = np.array([[Function(x[i + j]) for j in range(p)] for i in range(30 - p)])
    Real_line = np.array([Function(t) for t in x])
    Neuron_line = [np.dot(w, arr) for arr in matrix]
    error = Real_line[p:]-Neuron_line
    return sum([a**2 for a in error])

def Function(t):
    return 0.4 * math.sin(0.3 * t) + 0.5

def test_nu():
    error_list = []
    for i in np.arange(0.1, 1.1, 0.1):
        w = Train(6, 2000, i, False)
        error_list.append(Get_error(w, 6))
    plt.plot(np.arange(0.1, 1.1, 0.1), error_list)
    plt.xlabel("nu")
    plt.ylabel("Errors")
    plt.show()

def test_p():
    error_list = []
    for i in np.arange(1, 17):
        w = Train(i, 500, 0.4, False)
        error_list.append(Get_error(w, i))
    plt.plot(np.arange(1, 17), error_list)
    plt.xlabel("window")
    plt.ylabel("Errors")
    plt.show()

def test_era():
    error_list = []
    for i in np.arange(1000, 5000, 1000):
        w = Train(6, i, 0.4, False)
        error_list.append(Get_error(w, 6))
    plt.plot(np.arange(1000, 5000, 1000), error_list)
    plt.xlabel("Eras")
    plt.ylabel("Errors")
    plt.show()

        

if __name__ == "__main__":
    Train(5, 2000, 0.4)
    test_nu()
    test_p()
    test_era()

    #Lets_test(0, 2000)
    #   окно, эпох, график                             a+bx
    #окно 2 = 0.0069(50к) 3 = 0.0056(100к) 4 = 0.0013 5 = 9e-5 6 =  2e-6
