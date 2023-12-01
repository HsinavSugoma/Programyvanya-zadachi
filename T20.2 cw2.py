import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def perimeter(R, n):  # периметр n-кутника
    return 2 * n * np.sin(np.pi / n)

def pi(R, n):
    return perimeter(R, n) / (2 * R)

def update(k):
    ax.clear()
    ax.grid(True)  # додаєм сітку на графіку

    for i in range(len(k_v)): # зоображуємо n-кутник
        n = 2 ** k_v[i]
        a = np.linspace(0, 2 * np.pi, n + 1)
        x = np.cos(a) # координати по х
        y = np.sin(a) # координати по у
        ax.plot(x, y, label=f"{n} - кутник")

    ax.legend(loc='center')

if __name__ == "__main__":
    R = 1  # радіус кола
    k_v = np.arange(2, 10)  # k = 2, 3, 4..

    fig, ax = plt.subplots()  # створюємо вікно і вісі

    ani = FuncAnimation(fig, update)

    plt.show()
