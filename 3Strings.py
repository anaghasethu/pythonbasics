from email import message


name = "Anagha"
profession = 'Developer'
age = str(23)

print('My name is '+name+'. My profession is '+profession+'. My age is '+age)

print('Hi {name}!! Are you a {profession}..?'.format(name=name,profession=profession))

# String methods
message = "how are You"
print(message.capitalize())
print(message.casefold())
print(message.swapcase())

print(message.find('are'))