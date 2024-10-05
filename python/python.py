# Make some variables and store int, int array, int 2d array and strings datas.

int_var: int = 123
arr_var: list[int] = [1, 2, 3]
twdarr_var: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
str_var: str = 'Hello World'

print(int_var, arr_var, twdarr_var, str_var)

# Convert float to int, int to string and string to int. 

a = 12.56
b = int(a)
c = str(b)
d = int(c)

print(f'type of a({a}): {type(a)}\ntype of a({b}): {type(b)}\ntype of a({c}): {type(c)}\ntype of a({d}): {type(d)}\n')

# Get a string from user.

user_input = input('Enter string: ')

print(user_input)

# Print 5 random numbers using a for loop.

from random import randint
for i in range(5):
	print(randint(0, 10))




