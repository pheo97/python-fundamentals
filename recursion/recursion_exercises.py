def factorial_cal(num):
    if num == 0:
        return 1
    else:
        return num * factorial_cal(num - 1)


sum_fac = factorial_cal(5)
print("factorial:", sum_fac)


def fibonacci_sequence(num):
    if num < 1:
        return -1
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci_sequence(num - 1) + fibonacci_sequence(num - 2)


print("fibo nth term:", fibonacci_sequence(9))


def sum_all_nums(num):
    if num <= 0:
        return -1
    if num == 1:
        return num
    else:
        return num + sum_all_nums(num - 1)


print("sum:", sum_all_nums(5))
