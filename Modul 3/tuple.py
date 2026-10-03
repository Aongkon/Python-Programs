def multiple():
    return 3, 4
print(multiple()) #accidentally created tuple

things = 'pen', 'tripod', 'water bottle', 'charger', 'phone', 'web cam','sunglass'
print(type(things))
print(things[0])
print(things[-2])
print(things[3:6])
if 'phone' in things:
    print('exists')
for item in things:
    print(item)
