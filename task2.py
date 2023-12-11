from mylib import generate_random_numbers

print("Task #2")

my_list = generate_random_numbers(1, 20, 20)


def my_reverse(param_list):
    list_len = len(param_list)
    return list((num for num in param_list[list_len - 1::-1]))


print("Original List")
print(my_list)
print("Reversed List")
print(my_reverse(param_list=my_list))
