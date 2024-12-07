def print_max_min_rows(matrix):
    current_max_sum = sum(matrix[0])
    current_min_sum = current_max_sum

    for i in range(1, len(matrix)):
        row_sum = sum(matrix[i])
        if row_sum > current_max_sum:
            current_max_sum = row_sum
        if row_sum < current_min_sum:
            current_min_sum = row_sum

    for i in matrix:
        if sum(i) == current_max_sum:
            print(f"Строка с наибольшей суммой элементов: {i}, сумма элементов: {sum(i)}")
        if sum(i) == current_min_sum:
            print(f"Строка с наименьшей суммой элементов: {i}, сумма элементов: {sum(i)}")

matrix = [
    [4, 2, 4, 1],
    [4, 5, 1, 9],
    [7, 8, 9, 2],
    [15, 5, 2, 9]
]

print_max_min_rows(matrix)