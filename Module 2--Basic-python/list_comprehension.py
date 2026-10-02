numbers = [45, 87, 65, 43, 85, 14, 26, 61]
odds = []
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
print(odds)

odd_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(odd_nums)


# nested loop
plyers = ['shakib', 'musfik', 'tamim']
ages = [38, 37, 32]
age_comb = []
for player in plyers:
    print('player:', player)
    for age in ages:
        print(player, age)
        age_comb.append([player, age])
print(age_comb)

numbers= [7,6,5,3,3,2,1]
print(numbers[-4])