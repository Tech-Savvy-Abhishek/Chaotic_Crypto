# Importing necessary libraries
import math
import numpy as np

# Setting the parameters for the Kaplan-Yorke map
a = 1.5
b = 0.8

# Function to generate Kaplan-Yorke map


def generate_keplan_yorke_map(x0, y0, n):
    # Initialize an array to store the Kaplan-Yorke map
    keplan_yorke = np.zeros((n, 2))
    # Set the initial conditions
    keplan_yorke[0, 0] = x0
    keplan_yorke[0, 1] = y0

    # Generate the Kaplan-Yorke map
    for i in range(1, n):
        # Update x using the Kaplan-Yorke map equation
        keplan_yorke[i, 0] = a*keplan_yorke[i-1, 0] % 1
        # Update y using the Kaplan-Yorke map equation
        keplan_yorke[i, 1] = b*keplan_yorke[i-1, 1] + \
            math.cos(4*math.pi*keplan_yorke[i-1, 0])

    # Return the generated Kaplan-Yorke map
    return keplan_yorke[:, 0], keplan_yorke[:, 1]

# Initial conditions for the Kaplan-Yorke map
# x0 = 123457/3503377
# y0 = 765432/350377

# Generate the Kaplan-Yorke map
# x, y = generate_keplan_yorke_map(x0, y0, 10000)
