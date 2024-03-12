# Given an dict. Invert it (keys become values and values
# become keys). If there is more than key for that given
# value create an list.Input

ini_dict = { "a": 1, "b": 2, "c": 2 }
 
print("initial_dictionary", str(ini_dict))
 
flipped = {}
 
for key, value in ini_dict.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)
 
print("final_dictionary", str(flipped))