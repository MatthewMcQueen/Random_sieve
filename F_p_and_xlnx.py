import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

def euler_totient(p):
    return p - 1

def generate_primes(n):
    return list(sp.primerange(1, n + 1))

def plot_discrete_function(n):
    primes = generate_primes(n)
    x_values = list(range(1, len(primes) + 1))
    y_values = [euler_totient(p) for p in primes]

    plt.rcParams.update({
        'font.size': 14,
        'font.family': 'serif',
        'font.serif': 'Times New Roman'
    })

    plt.figure(figsize=(10, 10))
    plt.plot(x_values, y_values, marker='o', markersize=2, color='blue', linewidth=0.5, label='$Φ_P(x)$')

    x_ln_x = [x * np.log(x) for x in x_values]
    plt.plot(x_values, x_ln_x, color='red', label='$x ln(x)$')

    plt.xticks(ticks=range(0, n // 2 + 1, (n // 2) // 10))
    plt.yticks(ticks=range(0, n + 1, n // 10))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Відображення графіків $Φ_P(x)$ та $x ln(x)$')
    plt.grid(True)
    plt.legend()
    plt.xlim(0, n // 2)
    plt.ylim(0, n)
    plt.show()

n = 500
plot_discrete_function(n)