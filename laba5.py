def largest_power_of_two(num):
    power = 0
    result = 1
    
    while result <= num:
        power += 1
        result *= 2
    
    power -= 1
    result //= 2
    
    print("Показатель степени:", power)
    print("Наибольшая степень двойки:", result)

largest_power_of_two(int(input("N:")))