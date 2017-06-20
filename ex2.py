"""
Python Data types
Numbers,Lists,Tuples,Strings,and Dictionaries,Maps
"""

names = ['dennis',2,3,'80x86','James','lists']

un = ['mmu','Jkuat','MKU','KU','UoN']

marks = [12,42,16,25,70,'02',19,10,15]

print(names)
print(un)
print(marks)

print(un[2])
print(names[3])
print(marks[4])

""" slicing in python
use square brackets
syntax
[a:b]

: this is the slicing operator
"""

print(un[1:3])
print(un[:3])
print(un[1:])
print(un[:-3])
print(un[1:-2])

 new_list = names+un

print(new_list)

new_list = [names+un]

print(new_list)

