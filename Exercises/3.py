# Write a Python program to insert a new item before the second element in an existing array. 
# Sample Output:
# Original array: array('i', [1, 3, 5, 7, 9])
# Insert new value 4 before 3:
# New array: array('i', [1, 4, 3, 5, 7, 9])

numbers = [1, 3, 5, 7, 9]
add = 4
print(numbers)
numbers.insert(1,4)

print(numbers)
