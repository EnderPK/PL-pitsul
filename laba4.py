def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    m = int(input("Введите количество чисел Фибоначчи: "))
    fibonacci_numbers = list(generate_fibonacci(m))
    #print(fibonacci_numbers)
    total = sum(fibonacci_numbers)
    print("Сумма первых", m, "чисел Фибоначчи:", total)

if __name__ == "__main__":
    main()