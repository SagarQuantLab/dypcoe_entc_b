# convert list to dict 
# 1. dict & zip
# 2. for loop

key_list = ["Name", "Age", "Gender"]
value_list = ["Rohan", 35, "Male"]

# 1. using dict and zip
my_dict = dict(zip(key_list, value_list))

# 2. using for loop
my_dict = {}
for idx in range(len(key_list)):
    my_key = key_list[idx]
    my_value = value_list[idx]
    my_dict[my_key] = my_value

print(my_dict)
