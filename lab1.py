import numpy as np
import itertools
import matplotlib.pyplot as plt 
import math

#подсчет колва шагов при поиске комбинации
count = 0

#Обучение НС
def Train(logistic, select):
    global count
    count += 1
    nu = 0.3
    W = np.zeros(5, dtype = float)
    OutText = ''
    list_errors = []
    era = 0
    while not list_errors or list_errors[era - 1] > 0: #Начало эпохи
        if era == 50:
            break
        OutText += f'Era: {era}\nw: {", ".join([str(w) for w in np.around(W, 3)])}\n'
        era += 1
        errors = 0
        vector_y = []
        for i in select:
            net = np.dot(W, i)
            t = Function(i)
            y = Activate_func(logistic, net)
            vector_y.append(str(y))
            sigma = t - y
            if sigma != 0:
                errors += 1
                #корректировка весов
                W += [nu * sigma * Derivative_act_func(logistic, net) * xi for xi in i]
        OutText += f"Errors: {errors}\nVector: {', '.join(vector_y)}\n{'-' * 70}\n"
        list_errors.append(errors)
    #проверка обучения
    if Real_vector() == Neuron_vector(W, logistic):
        OutText += f"Test accessed\n{'*' * 70}\n"
        print(f'Step {str(count)}\nSelection:\n{[x[1:] for x in select]}\n{OutText}')
        count = 0
        Drow_plot(era, list_errors)
        return era
    else:
        print(f"{count}\nTest don't accessed\nNeuron can't learn\n{'*' * 70}")
        return None

#Вывод графика
def Drow_plot(era, list_errors):
    X = [i for i in range(era)]
    Y = [list_errors[i] for i in X]
    plt.plot(X, Y)
    plt.xlabel('Eras')
    plt.ylabel('Errors')
    plt.show()


#Выбор режима работы программы. Пороговая или логистическая. 
#Со всеми наборами или с минимальной выборкой
def Selection(isselect, islogistic):
    Set = [[1] + list(i) for i in itertools.product([0, 1], repeat = 4)]
    if not isselect:
        Train(islogistic, Set)
    else:
        for i in range(1, 16): #поиск минимальной обучающей выборки
            for rezult_selection in itertools.permutations(Set, i):
                if Train(islogistic, list(rezult_selection)) != None:
                    return None


#Булевый вектор, который высчитала НС
def Neuron_vector(W, logistic):
    out = []
    for i in [[1] + list(i) for i in itertools.product([0, 1], repeat = 4)]:
        net = np.dot(W, i)
        y = Activate_func(logistic, net)
        out.append(str(y))
    return ''.join(out)

#Функция активации
def Activate_func(logistic, net):
    if logistic:
        return 1 if 0.5 * (net / (1 + abs(net)) + 1) >= 0.5 else 0
    else:
        return 1 if net >= 0 else 0 #для пороговой

#Производная функции активации
def Derivative_act_func(logistic, net):
    return 1 / (2 * (abs(net) + 1) ** 2) if logistic else 1


#Реальный будевый вектор
def Real_vector():
    real = []
    for i in [[1] + list(i) for i in itertools.product([0, 1], repeat = 4)]:
        real.append(str(Function(i)))
    return ''.join(real)


#Функция, которой необходимо обучить НС
def Function(x):
    return int(not (x[1] or x[2]) or x[3] or x[4])


if __name__ == "__main__":
    #Пороговая на полном наборе
    Selection(False, False)
    #Логистическая на полном наборе
    Selection(False, True)
    #Пороговая на минимальной выборке
    Selection(True, False)
    #Логистическая на минимальной выборке
    Selection(True, True)
    