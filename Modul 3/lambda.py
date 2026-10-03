# def double(x):
#     return x*2

doubled = lambda num : num*2
squared = lambda num : num * num

result = doubled(44)
output = squared(3)
print(result)
print(output)

add = lambda a, b : a + b

sum = add(2, 6)
print(sum)


numbers = [12, 56, 98, 78, 26, 12, 6, 98]
doubled_num = map(doubled, numbers) # doubled er function onojaie numbers er man golo 2 diye gon hocche

doubled_num = map(lambda x: x*2, numbers)
squared_num = map(lambda x: x*x, numbers)
print(numbers)
# print(list(doubled_num))
print(list(squared_num))


actors = [
    {'name' : 'sabana', 'age' : 65},
    {'name' : 'sabnoor', 'age' : 45},
    {'name' : 'sabila noor', 'age' : 30},
    {'name' : 'srabonti', 'age' : 37},
    {'name' : 'shawon', 'age' : 47}
]

juniors = filter(lambda actor : actor['age'] < 40, actors)
fivers = filter(lambda actor : actor['age'] % 5 == 0, actors)
# print(list(juniors))
print(list(fivers))