def sayHello(name):
    print(f"Hey {name} How are you!!")

sayHello('Anagha')

# returning value

def getSum(num1,num2):
    total = num1+num2
    return total

print(getSum(4,8))

# lamda functions -  small anonymous function
getSq = lambda num : num * num
print(getSq(6))

def getDiff(num1,num2): return num1-num2
print(getDiff(6,4))

def fullName(first_name,last_name):
    return first_name+" " +last_name
print(fullName('Anagha','Sethu'))

getfullName = lambda f_name,l_name: f_name+ " "+ l_name
print(getfullName('Anagha','Sethu')) 

def getName(f_name,l_name): return f_name+ " " +l_name
print(getName('Anagha','Sethu'))