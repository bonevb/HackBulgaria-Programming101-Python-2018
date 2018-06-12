from copy import deepcopy


def matrix_bombing_plan():

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]
              ]

    rows = len(matrix)
    cols = len(matrix[0])

    xDirections = [0, 0, -1, 1, -1, 1, 1, -1]
    yDirections = [-1, 1, 0, 0, -1, 1, -1, 1]

    my_dict = dict()
    matrix_after_bombing = deepcopy(matrix)

    def valid_position(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        else:
            return True

    for i in range(rows):
        for j in range(cols):
            for p in range(8):
                if valid_position(i + xDirections[p], j + yDirections[p]):
                    matrix_after_bombing[i + xDirections[p]][j + yDirections[p]
                                                             ] = matrix[i + xDirections[p]][j + yDirections[p]] - matrix[i][j]

            for a in range(len(matrix_after_bombing)):
                for b in range(len(matrix_after_bombing[0])):
                    if matrix_after_bombing[a][b] < 0:
                        matrix_after_bombing[a][b] = 0

            my_dict[i, j] = sum([sum(i) for i in matrix_after_bombing])
            matrix_after_bombing = deepcopy(matrix)

    for key, value in my_dict.items():
        print(key, ':', value)


print(matrix_bombing_plan())
