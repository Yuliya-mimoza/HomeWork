# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt

a, b, c, d, e = -12, -18, 5, 10, -30
limit = 10
step = 0.01
line_style = '-'
direct_up = True
color = 'b'
step_acr=0.0000001


def switch_line():
    global line_style
    if line_style == '-':
        line_style = '--'
    else:
        line_style = '-'
    return line_style


def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color


def func(x):
    f = a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e
    return f


x = np.arange(-limit, limit+step, step)

X_modify = [(-limit, 'limit')]

for i in range(len(x)-1):
    if func(x[i]) > 0 and func(x[i+1]) < 0 or func(x[i]) < 0 and func(x[i+1]) > 0:
        x_acr=np.arange(x[i],x[i+1]+step_acr,step_acr)
        for j in range(len(x_acr)-1):
            if func(x_acr[j]) > 0 and func(x_acr[j+1]) < 0 or func(x_acr[j]) < 0 and func(x_acr[j+1]) > 0:
                X_modify.append((x_acr[j], 'zero'))
    if direct_up:
        if func(x[i]) > func(x[i+1]):
            direct_up = False
            X_modify.append((x[i], 'dir'))
    else:
        if func(x[i]) < func(x[i+1]):
            direct_up = True
            X_modify.append((x[i], 'dir'))


X_modify.append((limit, 'limit'))

print(X_modify)

for i in range(len(X_modify)-1):
    cur_x = np.arange(X_modify[i][0], X_modify[i+1][0]+step, step)
    if X_modify[i][1] == 'zero':
        plt.plot(X_modify[i][0], func(X_modify[i][0]), 'go')
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())


plt.grid()
plt.show()
