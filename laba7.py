def process_array(arr):
    if not arr:
        return {}

    max_val = max(arr)
    max_index = arr.index(max_val)

    odd_nums = [num for num in arr if num % 2 != 0]
    if not odd_nums:
        odd_nums = []

    odd_nums = sorted(odd_nums, reverse=True)

    return {
        "max_element": max_val,
        "max_index": max_index,
        "odd_numbers": odd_nums,
    }

arr = [3, 5, -2, 7, 1, -9, 4, -6]
result = process_array(arr)
print(f"Результат:")
print(f"  Максимальный элемент: {result['max_element']}, Порядковый номер: {result['max_index']}")
print(f"  Массив нечетных чисел в порядке убывания: {result['odd_numbers']}")