import numpy as np

def tr_vector(vector):
    v_1 = vector[vector < 0]
    v_2 = vector[vector >= 0]

    return np.hstack((v_1, v_2))

if __name__ == "__main__":
    v = input("Введіть компоненти вектора: ")
    vector = np.array([int(x) for x in v.split()])

    print(f"Перетворений вектор: {tr_vector(v)}")
