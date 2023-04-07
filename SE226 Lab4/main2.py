# Task 4a
dict = {}
for i in range(1, 31):
    dict[i] = (i - 1) * (i + 1)
print(dict)

# Task 4b
for k, v in dict.items():
    print(k, ":", v)

# Task 4c
total = 0
for v in dict.values():
    total += v
print("The sum of all values is:", total)

# Task 4d
num = int(input("Enter a number: "))
if num in dict:
    del dict[num]
    print("Item with key", num, "has been removed.")
else:
    print("The number entered is not a key in the dictionary.")
print(dict)
