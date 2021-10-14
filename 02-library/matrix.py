#implement a function called get_determinant()
#takes in a matrix (list of lists) and returns the determinant of the matrix

def get_determinant(matrix):
    total = 0
    idx = list(range(len(matrix)))

    if len(matrix) == 0:
        return 0
    elif len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        total = matrix[0][0] * matrix[1][1] - matrix [0][1] * matrix[1][0]
        return total
    elif len(matrix) == len(matrix[0]):
        for i in idx:
            new_matrix = matrix.copy()
            new_matrix = new_matrix[1:] #create sub_matrix

            for j in range(len(new_matrix)):
                new_matrix[j] = new_matrix[j][0:i] + new_matrix[j][i+1:]
            
            sign = (-1) ** (i%2)
            sub_det = get_determinant(new_matrix)
            total += sign * matrix[0][i] * sub_det
    else:
        raise ValueError("It must be a nxn matrix!")

    return total
