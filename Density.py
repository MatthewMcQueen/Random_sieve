import numpy as np
import matplotlib.pyplot as plt
import random

def generate_hawkins_primes(N):
    numbers = list(range(2, N+1))
    hawkins_primes = []
    while numbers:
        h = numbers.pop(0)
        hawkins_primes.append(h)
        numbers = [n for n in numbers if random.random() >= 1/h]
    return hawkins_primes

def plot_hawkins_primes(N, iterations):
    plt.figure(figsize=(10, 6))
    all_primes = []

    for i in range(iterations):
        primes = generate_hawkins_primes(N)
        all_primes.append(primes)

    all_primes.sort(key=len, reverse=True)

    for i, primes in enumerate(all_primes):
        x = primes
        y = [i+1] * len(primes)
        color = (255, min(255, i*(200/iterations)), min(255, i*(200/iterations)))  # RGB color adjustment
        color = tuple(c / 255.0 for c in color)  # Normalize color values
        plt.scatter(x, y, color=[color], s=1)  # Set even smaller size for points
        plt.text(N + 5, i+1, str(len(primes)), verticalalignment='center', color=color, fontsize=14, fontweight='bold', fontname='Times New Roman')  # Add text with the number of primes

    plt.xlabel('Значення', fontsize=16, fontweight='bold', fontname='Times New Roman')
    plt.ylabel('Ітерації', fontsize=16, fontweight='bold', fontname='Times New Roman')
    plt.title('Прості числа Гокінса', fontsize=18, fontweight='bold', fontname='Times New Roman')

    plt.yticks([])
    plt.xticks(np.arange(0, N+1, step=N/10))

    plt.show()

    for i, primes in enumerate(all_primes):
        print(f'Set {i+1}: {primes}')


N = 500
iterations = 15

plot_hawkins_primes(N, iterations)