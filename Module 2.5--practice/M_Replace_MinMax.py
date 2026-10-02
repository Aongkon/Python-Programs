n = int(input())
numbers = list(map(int, input().split()))
min_index = numbers.index(min(numbers)) # minimum index er man 
max_index = numbers.index(max(numbers)) # maximum index er man 

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
# print(min_index, max_index)
print(*numbers)