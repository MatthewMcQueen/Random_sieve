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


def plot_multiple_hawkins_functions(n, iterations):
    all_totients = []

    for _ in range(iterations):
        hawkins_primes_list = hawkins_primes(n)
        totients = [euler_totient(h) for h in hawkins_primes_list]
        all_totients.append(totients)

    max_length = max(len(t) for t in all_totients)
    sum_totients = np.zeros(max_length)
    count_totients = np.zeros(max_length)

    for totients in all_totients:
        for i in range(len(totients)):
            sum_totients[i] += totients[i]
            count_totients[i] += 1

    average_totients = sum_totients / np.maximum(count_totients, 1)

    plt.rcParams.update({
        'font.size': 14,
        'font.family': 'serif',
        'font.serif': 'Times New Roman'
    })

    plt.figure(figsize=(10, 10))

    colors = ['red', 'blue', 'green']
    labels = [f'$Φ_H^{(i)}(x)$' for i in range(1, iterations + 1)]

    for i in range(iterations):
        hawkins_primes_list = hawkins_primes(n)
        x_values_h = list(range(1, len(hawkins_primes_list) + 1))
        y_values_h = [euler_totient(h) for h in hawkins_primes_list]

        plt.plot(x_values_h, y_values_h, marker='o', markersize=0.05, linewidth=0.005, color=colors[i % len(colors)])

    x_avg = list(range(1, len(average_totients) + 1))
    plt.plot(x_avg, average_totients, marker='o', markersize=0.75, color='black', linewidth=0.3, label='Average $Φ_H(x)$')

    x_ln_x = [x * np.log(x) for x in range(1, n // 2 + 1)]
    plt.plot(range(1, n // 2 + 1), x_ln_x, color='red', linewidth=1, label='$x \ln(x)$')

    plt.xticks(ticks=range(0, n // 2 + 1, (n // 2) // 10))
    plt.yticks(ticks=range(0, n + 1, n // 10))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Відображення графіків $Φ_H(x)$, їх апроксимація для {iterations} випадкових наборів та $x ln(x)$')
    plt.grid(True)
    plt.xlim(0, n // 2)
    plt.ylim(0, n)
    plt.show()


n = 1000
iterations = 1000
plot_multiple_hawkins_functions(n, iterations)