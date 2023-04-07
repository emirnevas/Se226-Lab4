# Task 4a
divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

united_we_stand = dict()
united_we_stand.update(divided)
united_we_stand.update(we_fall)

print("Name", "Age")
for name, age in united_we_stand.items():
    print(name, age)

# Task 4b
united_we_stand_clone = united_we_stand.copy()
del united_we_stand_clone['Nat']
print("\nUpdated united_we_stand:")
print("Name", "Age")
for name, age in united_we_stand_clone.items():
    print(name, age)

# Task 4c
print("\nSorted united_we_stand:")
print("Name", "Age")
for name in sorted(united_we_stand.keys()):
    print(name, united_we_stand[name])

# Task 4d

values = list(united_we_stand.values())
max_value = values[0]
min_value = values[0]

for age in united_we_stand.values():
    if age > max_value:
        max_value = age
    if age < min_value:
        min_value = age

print("\nMaximum value: ", max_value)
print("Minimum value: ",  min_value)