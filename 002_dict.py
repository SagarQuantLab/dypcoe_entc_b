# DIct
# {}, key, ordered, no duplicates allowed, mutable

my_dict = {
    "Name": "Rohan",
    "Age": 35,
    "Gender": "Male",
}

# access the value Rohan
print(my_dict['Name'])

# access all the keys
print(my_dict.keys())

# access all the values
print(my_dict.values())

# access all the items
print(my_dict.items())

# change age to 25
my_dict["Age"] = 25
print(my_dict)


###########################################################
# ITEMS  ACCESS     SYMBOLS    ORDERED     DUPLCIATES    MUTABLE
# LIST    Index         []       Y          Y               Y
# DICT     Key          {}       Y          N               Y
# TUPLE   Index         ()       Y          Y               N
# SETS      -           {}       N          N               N

# {}, key, ordered, no duplicates allowed, mutable