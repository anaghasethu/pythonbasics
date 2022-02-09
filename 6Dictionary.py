# Colection - unordered, changeable and indexed
# no duplicate members

from itertools import product


person = {
    'first_name': 'Anagha',
    'last_name': "Sethu",
    'age':23
}
# using constructor
person2 = dict(first_name = 'Ahana',last_name='Sethu',age=28)

print(person,type(person))
print(person2,type(person2))

person['phone'] = '9836289280'

print(person)
print(person.values())
print(person.items())
del(person['age'])
print(person)

# using list of dictionary
products = [
    {
        'Name': 'White Tshirt',
        'Category': 'Womens Dress'
    },
    {
        'Name': 'Huawei Y9 Prime 2019',
        'Category': 'Mobiles'
    },
    {
        'Name': 'Black sneakers',
        'Categeory': 'Mens footwear'
    }
]

print(products[1]['Category'])