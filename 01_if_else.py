# if
my_age = 19

# if
if my_age > 18:
    print("Adult")

# if else
if my_age > 18:
    print("Adult")
else:
    print("Minor")

# if elseif else
if my_age > 18:
    print("Adult")
elif my_age == 18:
    print("Turning adult")
else:
    print("Minor")

# reduce lines
msg = "Bye"
if isinstance(my_age, int):
    msg = "hello"

print(msg)
