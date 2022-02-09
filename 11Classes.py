# create class
class user:
    # create constructor
    def __init__(self,name,city,id) :
        self.name = name
        self.city = city
        self.id = id
    def greetings(self):
        return f'My name is {self.name}'
# init user object

Anagha = user("Sethu","palakkad",34)

print(Anagha.id)
print(Anagha.greetings())

# extend class
class customer(user):
    def __init__(self,name,city,id) :
        self.name = name
        self.city = city
        self.id = id
    def set_balance(self,balance):
        self.balance = balance

# initialise customer
custo = customer("Anagha","Kerala",103562)
custo.set_balance(18927323)
print(custo.greetings())