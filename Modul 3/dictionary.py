# key value pair
person = {'name' : 'kala pakhi', 'address' : 'kaliapur', 'age' : 23, 'job' : 'bekar'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = "python" # add kora jay
person['name'] = 'sada pakhi' # update kora jay
print(person.keys())
print(person.values())

for key, val in person.items():
    print(key,':', val)
