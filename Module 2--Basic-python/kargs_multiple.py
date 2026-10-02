def full_name(first, last):
    name = f'full name is: {first} {last}' 
    return name

# name = full_name('alu', 'kodu')
name = full_name(last = 'kodu', first='alu')
print(name)

# key arguments
def famous_name(first, last, **addition):
    new_name = f'the name is: {first} {last}'
    print(addition)
    print(addition['title'])
    for key, value in addition.items():
        print(f'key or val: {key} {value}')
    return new_name
new_name = famous_name(first='tahel', last='ali', title='chor', title2='vhondo', last2='taheri')
print(new_name)


def all_of(num1, num2):
    res1 = num2 - num1
    res2 = num1 + num2
    res3 = num2 * num1
    return res1, res2, res3

final = all_of(56, 42)
print (f'that is final val: {final}')