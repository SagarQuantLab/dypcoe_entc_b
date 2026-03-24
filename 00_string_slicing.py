my_string = "Hello this is ENTC students"

# access first letter
print(my_string[0])

# first word 'Hello'
print(my_string[0:5])

# first word with interval of 2
print(my_string[0:5:2])

# access last letter
print(my_string[-1])

# second last letter
print(my_string[-2])

# reverse string
print(my_string[::-1])

# reverse students
print(my_string[:-9:-1])

# replace string
replaced_string = my_string.replace("s", "X")
print(replaced_string)

# upper case or lower case
print(my_string.upper())
print(my_string.lower())