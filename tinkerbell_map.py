# Importing necessary library
import numpy as np

# Setting the parameters for the Tinkerbell map
a = 0.9
b = -0.6013
c = 2
d = 0.5

# Function to generate Tinkerbell map


def generate_tinkerbell_map(x0, y0, n):
    # Initialize an array to store the Tinkerbell map
    tinkerbell = np.zeros((n, 2))
    # Set the initial conditions
    tinkerbell[0, 0] = x0
    tinkerbell[0, 1] = y0

    # Generate the Tinkerbell map
    for i in range(1, n):
        # Update x and y using the Tinkerbell map equations
        tinkerbell[i, 0] = tinkerbell[i-1, 0]**2 - tinkerbell[i-1, 1]**2 \
            + a*tinkerbell[i-1, 0] + b*tinkerbell[i-1, 1]
        tinkerbell[i, 1] = 2*tinkerbell[i-1, 0]*tinkerbell[i-1, 1] \
            + c*tinkerbell[i-1, 0] + d*tinkerbell[i-1, 1]

    # Return the generated Tinkerbell map
    return tinkerbell[:, 0], tinkerbell[:, 1]

# Initial conditions for the Tinkerbell map
# x0 = -0.72
# y0 = -0.64

# Generate the Tinkerbell map
# x, y = generate_tinkerbell_map(x0, y0, 100)
