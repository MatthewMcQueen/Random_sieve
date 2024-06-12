import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import random

def euler_totient(n):
    if n == 1:
        return 1
    result = n
    for p in sp.primefactors(n):
        result *= (1 - 1 / p)
    return int(result)

def hawkins_primes(n):
    numbers = list(range(2, n + 1))
    hawkins_primes_list = []

    while numbers:
        h = numbers.pop(0)
        hawkins_primes_list.append(h)
        numbers = [x for x in numbers if random.random() >= 1 / h]

    return hawkins_primes_list

def plot_multiple_hawkins_functions(n):
    colors = ['red', 'blue', 'green']
    labels = ['$Φ_H^{(1)}(x)$', '$Φ_H^{(2)}(x)$', '$Φ_H^{(3)}(x)$']

    plt.rcParams.update({
        'font.size': 14,
        'font.family': 'serif',
        'font.serif': 'Times New Roman'
    })

    plt.figure(figsize=(10, 10))

    for color, label in zip(colors, labels):
        hawkins_primes_list = hawkins_primes(n)
        x_values_h = list(range(1, len(hawkins_primes_list) + 1))
        y_values_h = [euler_totient(h) for h in hawkins_primes_list]

        plt.plot(x_values_h, y_values_h, marker='o', markersize=5, color=color, linewidth=1, label=label)
        print(f"Прості числа Гокінса для {label}:", hawkins_primes_list)

    plt.xticks(ticks=range(0, n // 2 + 1, (n // 2) // 10))
    plt.yticks(ticks=range(0, n + 1, n // 10))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Відображення графіків $Φ_H^{(1)}(x)$, $Φ_H^{(2)}(x)$ та $Φ_H^{(3)}(x)$')
    plt.grid(True)
    plt.legend()
    plt.xlim(0, n // 2)
    plt.ylim(0, n)
    plt.show()

n = 50
plot_multiple_hawkins_functions(n)