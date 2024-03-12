def calculate_sum(n):
    sum1 = sum([i**5 for i in range(1, n+1)])
    sum2 = sum([i**7 for i in range(1, n+1)])
    sum3 = sum([i for i in range(1, n+1)])
    result = 2 * (sum3**4)
    return sum1 + sum2, result

N = 10  # Задайте значение N
result_sum, expected_result = calculate_sum(N)
print(f"Сумма левой части: {result_sum}")
print(f"Правая часть: {expected_result}")
print(f"Равны ли значения: {result_sum == expected_result}")
