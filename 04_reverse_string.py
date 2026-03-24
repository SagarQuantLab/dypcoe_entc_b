# how to reverse a string?
# 1. String slicing
# 2. Reverse function
# 3. for loop

# define string
my_string = "hello this is ENTC students"

# 1. string slicing
reversed_string = my_string[::-1]

# 2. reverse function
reversed_string = "".join(reversed(my_string))

# 3. for loop
reversed_string = ""
for each_char in my_string:
    reversed_string = each_char + reversed_string