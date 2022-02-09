# Tuples - ordered and unchangable
# allows duplicate members

from ctypes import c_size_t


fruits = ('Apple','Orange','Grape')

print(fruits,type(fruits))


c_set = { 'Java','Mysql','Python'}
c_set.add('JS')
print(c_set)
c_set.clear()
print(c_set)