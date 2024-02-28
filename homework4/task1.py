def transpose(matrix: list) -> None:
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    matr = [[1, 2, 3, 0], [4, 5, 6, -1], [7, 8, 9, -2], [-3, -4, -5, -6]]
    print(matr)
    transpose(matr)
    print(matr)
