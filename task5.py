from mylib import generate_random_numbers, get_even_in_list, get_odd_in_list

my_list = generate_random_numbers(1, 100, 10)


user_input = int(input("Enter a number, 1 for odd , 2 for even: "))
if user_input not in [1, 2]:
    print("Invalid value, should be 1 or 2")
    exit()

filtered_number = None
if user_input % 2 == 0:
    even_or_odd = "even"
    filtered_number = get_even_in_list(my_list)
else:
    even_or_odd = "odd"
    filtered_number = get_odd_in_list(my_list)


print(f"The summation of all {even_or_odd} numbers is {sum(filtered_number)}")
print("Source List")
print(my_list)
print("Filtered Numbers")
print(filtered_number)
