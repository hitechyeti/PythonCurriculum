def get_diagonals(matrix):
    row_count = len(matrix)

    main_diag = []
    second_diag = []
    for i in range(row_count):
        # top-left to bottom-right
        main_diag.append(matrix[i][i])
        # top-right to bottom-left
        second_diag.append(matrix[i][row_count-i-1])
    return (main_diag,second_diag)


def get_diagonals(matrix):
    length = len(matrix[0])
    d1 = [matrix[i][i] for i in range(length)]
    d2 = []
    cnt = length - 1
    for i in range(length):
        d2.append(matrix[i][cnt])
        cnt -= 1
    return (d1,d2)
