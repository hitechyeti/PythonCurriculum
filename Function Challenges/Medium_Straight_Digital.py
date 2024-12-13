def is_straight_digital(n):
    diff = []
    for i in range(len(str(n))-1):
        diff.append(int(str(n)[i+1]) - int(str(n)[i]))
    if diff.count(diff[0]) ==len(diff):
        return True
    return False


def is_straight_digital(n):
    n = str(n)
    difference = int(n[1])-int(n[0])
    for i in range(2, len(n)):
        if int(n[i])-int(n[i-1]) != difference:
            return False
    return True


def is_straight_digital(n):
    n_str = str(n)  # Convert the number to a string
    if len(n_str) < 2:  # Single-digit numbers automatically qualify
        return True

    # Calculate the difference between the first two digits
    diff = int(n_str[1]) - int(n_str[0])

    # Check if all consecutive digits have the same difference
    for i in range(len(n_str) - 1):  # Loop through all pairs of consecutive digits
        if int(n_str[i + 1]) - int(n_str[i]) != diff:
            return False  # Return False if any difference mismatches

    return True  # If loop completes, all differences are the same


