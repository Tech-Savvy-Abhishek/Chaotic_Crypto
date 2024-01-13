# Importing necessary libraries
import numpy as np

# Setting the parameters for the Henon map
a = 1.4
b = 0.3

# Function to generate henon map


def generate_henon_map(x0, y0, n):
    # Initialize an array to store the Henon map
    henon = np.zeros((n, 2))
    # Set the initial conditions
    henon[0, 0] = x0
    henon[0, 1] = y0

    # Generate the Henon map
    for i in range(1, n):
        # Update x and y using the Henon map equations
        henon[i, 0] = 1 - a * henon[i-1, 0]**2 + henon[i-1, 1]
        henon[i, 1] = b * henon[i-1, 0]

    # Return the generated Henon map
    return henon[:, 0], henon[:, 1]

# Initial conditions for the Henon map
# x0 = 0.1
# y0 = 0.1

# Generate the Henon map
# x, y = generate_henon_map(x0, y0, 1000)
