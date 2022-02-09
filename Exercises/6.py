# Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

str = "1234abcd"

print(str)
rev = ""
for i in str:
    rev = i + rev

print(rev)
