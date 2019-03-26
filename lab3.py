import numpy as np
import itertools
import matplotlib.pyplot as plt 
import math

def RBF():
    number_of_1 = [Function(i) for i in itertools.product([0, 1], repeat = 4)].count(1)
    if number_of_1 <=8:
        return [i for i in itertools.product([0, 1], repeat = 4) if Function(i)]
    else:
        return [i for i in itertools.product([0, 1], repeat = 4) if not Function(i)]

def Train(selection):
    nu = 0.3
    c = RBF() #RBF-нейроны
    u = np.zeros(len(c) + 1, float)
    era = 0
    error_list = []
    OutText = ''
    while not error_list or error_list[era - 1] > 0:
        OutText += f'Era: {era}\nw: {u}\n'
        era += 1
        errors = 0
        vector_y = []
        for x in selection:
            fi = Compute_fi(c, x)
            t = Function(x)
            net = np.dot(fi, u)
            y = 1 if net >= 0 else 0
            vector_y.append(str(y))
            sigma = t - y
            if not sigma == 0:
                errors += 1
                u += [nu * sigma * fi_i for fi_i in fi]
        OutText += f"Errors: {errors}\nVector: {''.join(vector_y)}\n{'-' * 70}\n"
        error_list.append(errors)
    #test for verify neuron
    if Neuron_vector(c, u) == Real_vector():
        print(f"Selection: {selection}\n{OutText}Test accessed\n{'*' * 70}")
        Drow_plot(era, error_list)
        return era
    else:
        print(f"\nTest don't accessed\nNeuron can't learn\n{'*' * 70}")
        return 50

def Drow_plot(era, list_errors):
    X = [i for i in range(era)]
    Y = [list_errors[i] for i in X]
    plt.plot(X, Y)
    plt.xlabel('Eras')
    plt.ylabel('Errors')
    plt.show()

#будевый вектор, который высчитал нейрон
def Neuron_vector(c, u):
    out = ''
    for x in [list(i) for i in itertools.product([0, 1], repeat = 4)]:
        fi = Compute_fi(c, x)
        net = np.dot(fi, u)
        y = 1 if net >= 0 else 0
        out += str(y)
    return out

#реальный будевый вектор
def Real_vector():
    real = ''
    for i in [list(i) for i in itertools.product([0, 1], repeat=4)]:
        real+=str(Function(i))
    return real

#значения в RBF-нейронах
def Compute_fi(c, x):
    difference= [[np.array(x) - np.array(ci)] for ci in c]
    return [1] + [math.exp(-np.sum(np.power(diff, 2))) for diff in difference]

def Function(x):
    return int(not (x[0] or x[1]) or x[2] or x[3])

def Selection():
    Set = [list(i) for i in itertools.product([0, 1], repeat=4)]
    for i in range(1, 16): #поиск минимальной обучающей выборки
            for rezult_selection in itertools.permutations(Set, i):
                if Train(list(rezult_selection)) < 50:
                    return None

if __name__ == "__main__":
    selection =  [[0, 0, 0, 1], [1, 1, 0, 0]]
    Train(selection)