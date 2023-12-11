import random


print("Task #1")

my_list = []

for index in range(0, 10):
    my_list.append(random.randint(1, 100))

for index, element in enumerate(my_list):
    print(f"Index: {index} Value: {element}")


counter = 0
for even_number in (element for element in my_list if element % 2 == 0):
    old_counter = counter
    counter += even_number
    print(f"{str(even_number).ljust(4, ' ')} + {str(old_counter).ljust(4, ' ')} = {counter}")

print("=" * 18)
# sum only the even numbers
even_numbers = sum(element for element in my_list if element % 2 == 0)
print(f"TOTAL         {even_numbers}")
