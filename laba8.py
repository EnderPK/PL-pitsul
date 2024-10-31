def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    gcd_value = gcd(numerator, denominator)
    return numerator // gcd_value, denominator // gcd_value

def divide_fractions(numerator1, denominator1, numerator2, denominator2):
    if denominator1 == 0 or denominator2 == 0:
        raise ZeroDivisionError("Деление на ноль!")
    
    lcm_numerator = (numerator1 * numerator2)
    lcm_denominator = (denominator1 * denominator2)
    lcm=gcd(lcm_numerator, lcm_denominator)
    
    return simplify_fraction(lcm_numerator/lcm, lcm_denominator/lcm)

# Тестовые данные
numerator1, denominator1 = 1, 2
numerator2, denominator2 = 72, 4
result_numerator, result_denominator = divide_fractions(numerator1, denominator1, numerator2, denominator2)

print(f"Результат: {result_numerator}/{result_denominator}")

# We can push all homeworks (including those two) to my github.