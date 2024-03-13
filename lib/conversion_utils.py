# Function to convert a list of integers to a binary sequence
def list_to_binary(lst):
    # Initialize an empty string to hold the binary sequence
    binary_sequence = ''
    # Iterate over each number in the list
    for num in lst:
        # Convert the number to binary and pad it to 8 bits
        binary_num = format(num, '08b')
        # Add the binary number to the binary sequence
        binary_sequence += binary_num
    # Return the binary sequence
    return binary_sequence

# Function to convert henon map values to an integer and then to a binary sequence


def henon_to_binary(He1, He2):
    # Convert the He2 values to a list
    He = He2.tolist()
    # Remove the first element from the list
    He.pop(0)
    # Iterate over each value in the list
    for i in range(len(He)):
        # Scale the value, convert it to an integer, and take the modulus 256
        He[i] = int(He[i]*10**15) % 256
    # Convert the list of integers to a binary sequence
    str1 = list_to_binary(He)
    # returns the binary sequence
    return str1


# Function to convert Kaplan-Yorke map values to a binary sequence
def kaplan_yorke_to_binary(Ka1, Ka2):
    # Convert the Ka2 values to a list
    Ka = Ka2.tolist()
    # Remove the first element from the list
    Ka.pop(0)
    # Iterate over each value in the list
    for i in range(len(Ka)):
        # Scale the value, convert it to an integer, and take the modulus 256
        Ka[i] = int(Ka[i]*10**15) % 256
    # Convert the list of integers to a binary sequence
    str2 = list_to_binary(Ka)
    # Return the binary sequence
    return str2


# Function to convert Tinkerbell map values to a binary sequence
def tinkerbell_to_integer(Tn1, Tn2):
    # Convert the Tn2 values to a list
    Tn = Tn2.tolist()
    # Remove the first element from the list
    Tn.pop(0)
    # Iterate over each value in the list
    for i in range(len(Tn)):
        # Scale the value, convert it to an integer, and take the modulus 256
        Tn[i] = int(Tn[i]*10**15) % 256
        # Take the modulus 16 of the result. This effectively limits the values to the range 0-15.
        Tn[i] = Tn[i] % 16
    # Return the integer list
    return Tn
