# Write a Python program to get the number of occurrences of a specified element in an array
# Sample Output:
# Original array: array('i', [1, 3, 5, 3, 7, 9, 3])
# Number of occurrences of the number 3 in the said array: 3

numbers = [1, 3, 5, 3, 7, 9, 3]
i = 3
j=0
count = 0 
len = len(numbers)
print(numbers)
while j<len:
    if i == numbers[j]:
        count=count+1
    j = j+1
print(count)
