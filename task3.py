from mylib import generate_random_numbers

print("Task #3")

my_list = generate_random_numbers(1, 10, 10)
print(my_list)

user_input = str(input("Input number: "))
found_element = next({"num": num, "index": index} for index, num in enumerate(
    my_list) if num == int(user_input))

if found_element:
    print(
        f"Number({user_input}) found in the list at index {found_element['index']}.")
else:
    print(f"Number({user_input}) not found in the list.")
