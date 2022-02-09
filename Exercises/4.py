#  Write a Python function that takes a list of words and return the longest word and the length of the longest one
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

def findlongest():
    max = len(str[0])
    longest = str[0]

    for i in str:
        if max < len(i):
            longest = i
            max = len(i)
    print("Longest word: ",longest)
    print("Length of the longest word: ",max)


str = ["hello","hi","longest","short"]

findlongest()