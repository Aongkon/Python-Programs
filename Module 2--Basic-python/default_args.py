# args
def all_sum(num1, num2, *numbers):
    print('its a number:', num1)
    print(numbers) # ekhane tupple ba set akare value nicche
    sum = 0
    for num in numbers:
        print(num)
        sum = num + sum
    return sum

total = all_sum(34, 56, 67, 45, 67, 34)
print('all sum: ', total)