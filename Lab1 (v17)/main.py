#lab1
import numpy as np
import matplotlib.pyplot as plt


def compute_y(x, c, p):
    inner_expression = np.sqrt(x**2 * c**2 + p**2) - x**2 - (c**2 / 4)
    
    if inner_expression >= 0:
        y = np.sqrt(inner_expression)
    else:
        y = None
    
    return y

def plot(c, p, title):
    x_values = np.linspace(-2 * c, 2 * c, 1000)

    y_values_positive = []
    y_values_negative = []
    valid_x_values = []
    
    for x in x_values:
        y = compute_y(x, c, p)
        if y is not None:
            valid_x_values.append(x)
            y_values_positive.append(y)
            y_values_negative.append(-y)

    plt.figure(figsize=(8, 6))
    plt.scatter(valid_x_values, y_values_positive, label=f'Upper part, p = {p}', color='blue', s=1)
    plt.scatter(valid_x_values, y_values_negative, label=f'Lower part, p = {p}', color='orange', s=1)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(-c / 2, color='red', linestyle='--', label='Point A')
    plt.axvline(c / 2, color='green', linestyle='--', label='Point B')

    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()


c = 10 
c2_div_4 = (c ** 2) / 4  # c^2 / 4
c2_div_2 = (c ** 2) / 2  # c^2 / 2

plot_with_compute_y(c, c2_div_4, "Випадок 1: p = c^2 / 4")
plot_with_compute_y(c, c2_div_4 / 2, "Випадок 2: p < c^2 / 4")
plot_with_compute_y(c, (c2_div_4 + c2_div_2) / 2, "Випадок 3: c^2 / 4 < p < c^2 / 2")
plot_with_compute_y(c, c2_div_2, "Випадок 4: p > c^2 / 4")

a = int(input("Your p: "))
c_new = int(input("Your c: "))
plot_with_compute_y(c_new, a, f"Випадок 5: p = {a}")