# frequency of a specific number in an array

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
