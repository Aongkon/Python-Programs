# list = []
# tuple = ()
# set = {}
numbers = [12, 56, 98, 78, 56, 12, 6, 98]
print(numbers)
number_set = set(numbers)
print(number_set) #unique items collection. No duplicate
number_set.add(55)
number_set.add(12)
number_set.add(12)
number_set.remove(6)
for item in number_set:
    print(item)
if 9 in number_set:
    print('9 exists')
elif 98 in number_set:
    print('98 exists')