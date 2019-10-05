# Dictionary
school = {"math":"270", "physics":"320", "comsci":"480", "engineering":"360"}
math_st = school["math"]         # Access an item by its key
school["comsci"] += 20           # Modify an item through its key
school["maphy"] = 100            # Add another item
school["art"] = 100              # Add another item
print(len(school))               # Check the size of the dictionary
school.pop("art")                # Delete an item

cva  = school.copy()             # Copy dictionary, cva = school doesnt work :)  
khtn = dict(school)
ams  = dict(cva)

hanoi = {"cva":cva, "khtn":khtn, "ams":ams}    # Nested dictionary

for major in school:
    print(major)                 # print all key names
    print(school[major]          # print all values

for major, nost in school.items():
    print(major, nost)           # Prit both key and value of all items
	
