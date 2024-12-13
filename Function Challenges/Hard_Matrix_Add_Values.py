def add_matrix_values(matrix):
    total = None
    current_op = None
    for row in matrix:
        for item in row:
            if isinstance(item, (int, float)):
                if total is None:
                    total = item
                else:
                    if current_op == '+':
                        total += item
                    elif current_op == '-':
                        total -= item
                    elif current_op == '*':
                        total *= item
                    elif current_op == '/':
                        total /= item
            else:
                current_op = item
    return(total)
