import random


def generate_random_numbers(min, max, size):
    if min >= max:
        raise ValueError("Min should less than max!")

    uniq_list = []
    while len(uniq_list) < size:
        rand_mum = random.randint(min, max)
        if rand_mum not in uniq_list:
            uniq_list.append(rand_mum)

    return uniq_list


def get_even_in_list(param_list):
    if isinstance(param_list, list) == False:
        raise TypeError("param_list should be a list!")

    return [num for num in param_list if num % 2 == 0]


def get_odd_in_list(param_list):
    if isinstance(param_list, list) == False:
        raise TypeError("param_list should be a list!")

    return [num for num in param_list if num % 2 != 0]


def fibonacci(num):
    numbers = []
    for index, n in enumerate(range(0, num+1)):
        if index in [0, 1]:
            numbers.append(n)
        else:
            numbers.append(numbers[index-1]+numbers[index-2])

    return numbers


def sum_fibonacci(num):
    fib_list = fibonacci(num)
    return sum(fib_list)
