
# basic functions of dictionary

# dictionary in python is a set of key->value pairs

# id -> name
my_class = dict({202514:'ron', 202515:'alton', 202516:'ycm', 202517:'ax'})
print(my_class)
print(my_class.keys())
print(my_class.values())

for k,v in my_class.items():
    print("key is",k,", value is",v)

# accessing one element in the dictionary
print(my_class[202514])

# add a new element to the dictionary
my_class[111111] = 'guest'
print(my_class[111111])

guest_id = 111111
if guest_id in my_class:    # test whether the given key exists in the dictionary
    print('in my class')
else:
    print('not in my class')

# remove an element from the dictionary
my_class.pop(guest_id)

if guest_id in my_class:    # test whether the given key exists in the dictionary
    print('in my class')
else:
    print('not in my class')

print(len(my_class))
