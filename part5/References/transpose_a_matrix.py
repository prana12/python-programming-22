def transpose(matrix: list):
    transposed = [None]*len(matrix[0])
    for t in range(len(matrix)):
        transposed[t] = [None]*len(matrix)
        for tt in range(len(matrix[t])):
            transposed[t][tt] = matrix[tt][t]
    print_matrix(transposed)

def print_matrix(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            item = matrix[i][j]
            print(f"{item} ", end="")
        print()

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(matrix)
    print()
    transpose(matrix)