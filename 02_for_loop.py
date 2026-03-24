for i in range(5):
    print(i)

for i in range(0, 5):
    print(i)

for i in range(0, 5, 1):
    print(i)

my_list = [1, 4, 5, 8, 3, 3]
for idx in range(len(my_list)):
    print(idx)

for idx in range(len(my_list)):
    print(my_list[idx])

for each_element in my_list:
    print(each_element)

idx = 0
for each_element in my_list:
    print(each_element, idx)
    idx += 1

for idx, each_element in enumerate(my_list):
    print(idx, each_element)

my_dict = {
    "Name":"Rohan",
    "Age": 35,
    "Gender": "Male"
    }

# display each key
for each_key in my_dict.keys():
    print(each_key)

# display each value
for each_value in my_dict.values():
    print(each_value)

# access each items
for each_item in my_dict.items():
    print(each_item)

# access value from keys
for each_key in my_dict.keys():
    print(each_key, my_dict[each_key])