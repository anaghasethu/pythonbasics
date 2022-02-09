# Write a Python function to sum all the numbers in a list
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

numbers = list((8, 2, 3, 0, 7))

sum = 0
for i in numbers:
    sum = sum + i
print(sum)