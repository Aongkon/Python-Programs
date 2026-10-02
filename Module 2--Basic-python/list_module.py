numbers = [12, 45, 98, 68]
numbers.append(40)
print(numbers)
numbers.insert(2, 77)
print(numbers)
if 98 in numbers:
    numbers.remove(98)
if 8 in numbers:
    numbers.remove(8)
print(numbers)

last = numbers.pop()
print(last, numbers)

if 5 in numbers:
    index = numbers.index(5)
    print(index)

sorted = numbers.sort()
print(numbers)