def print_max_min_rows(matrix):
    current_max_sum = sum(matrix[0])
    current_min_sum = current_max_sum

    for i in range(1, len(matrix)):
        row_sum = sum(matrix[i])
        if row_sum > current_max_sum:
            current_max_sum = row_sum
        if row_sum < current_min_sum:
            current_min_sum = row_sum

    return current_max_sum, current_min_sum


def digi2sign(matrix):
    err = 0
    prv = len(matrix[0])
    for row in matrix:
        err += len(row) != prv
        prv = len(row)
    err += len(matrix) != prv
    if not err:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] >= 0:
                    matrix[i][j] = 1
                elif matrix[i][j] < 0:
                    matrix[i][j] = 0
    else:
        print("Non-square.")
        raise ValueError


def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.split())) for line in lines]
    return matrix

def write_matrix_to_file(matrix, filename):
    with open(filename, 'a') as file:
        for row in matrix:
            file.write(', '.join(map(str, row)) + '\n')

def write_text_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text + '\n')


input_filename = 'ПицулКонстантинАндреевич_У-242_vvod.txt'
output_filename = 'ПицулКонстантинАндреевич_У-242_vivod.txt'

matrix = read_matrix_from_file(input_filename)

max_sum, min_sum = print_max_min_rows(matrix)
txt=""
for i in matrix:
    if sum(i) == max_sum:
        txt += f"Строка с наибольшей суммой элементов: {i}, сумма элементов: {max_sum}" + "\n"
    if sum(i) == min_sum:
        txt += f"Строка с наименьшей суммой элементов: {i}, сумма элементов: {min_sum}" + "\n"

write_text_to_file(txt, output_filename)

digi2sign(matrix)
write_matrix_to_file(matrix, output_filename)