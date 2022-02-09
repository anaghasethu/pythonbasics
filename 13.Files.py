# open files

myFile = open('myfile.txt','w')

print(myFile.name)
print(myFile.closed)
print(myFile.mode)

myFile.write('Hey How are you..?')
myFile.close()
open('myfile.txt')