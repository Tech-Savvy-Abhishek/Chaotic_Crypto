import matplotlib.pyplot as plt
import numpy as np
from henon_map import generate_henon_map
from kaplan_yorke_map import generate_keplan_yorke_map
from tinkerbell_map import generate_tinkerbell_map

# Use a different style for the plots
plt.style.use('seaborn-darkgrid')


def generate_and_plot_henon_map(x0, y0, n):
    # Generate the Henon map
    x, y = generate_henon_map(x0, y0, n)

    # Plot the output
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, s=1, c='blue', alpha=0.5)
    plt.title('Henon Map', fontsize=20)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    plt.show()


def generate_and_plot_kaplan_yorke_map(x0, y0, n):
    # Generate the Kaplan-Yorke map
    x, y = generate_keplan_yorke_map(x0, y0, n)

    # Plot the output
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, s=1, c='green', alpha=0.5)
    plt.title('Kaplan-Yorke Map', fontsize=20)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    plt.show()


def generate_and_plot_tinkerbell_map(x0, y0, n):
    # Generate the Tinkerbell map
    x, y = generate_tinkerbell_map(x0, y0, n)

    # Plot the output
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, s=1, c='red', alpha=0.5)
    plt.title('Tinkerbell Map', fontsize=20)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    plt.show()

# The resulting plot should show a characteristic shape known
# as a strange attractor if the implementation is correct.


# Call the function with initial conditions x0 = 0.1, y0 = 0.1, and n = 10000
generate_and_plot_henon_map(0.1, 0.1, 10000)

# Call the function with initial conditions x0 = 123457/3503377, y0 = 765432/350377, and n = 10000
generate_and_plot_kaplan_yorke_map(123457/3503377, 765432/350377, 10000)

# Call the function with initial conditions x0 = -0.72, y0 = -0.64, and n = 10000
generate_and_plot_tinkerbell_map(-0.72, -0.64, 10000)
