def print_digits_reversed(n):
    if n == 0:
        return
    else:
        print(n % 10, end=" ")
        print_digits_reversed(n // 10)

M = 56789
print_digits_reversed(M)