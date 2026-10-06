n = input()
number_list = list(map(int, input().split()))

# min_val = min(number_list)
# max_val = max(number_list)

min_idx = number_list.index(min(number_list))
max_idx = number_list.index(max(number_list))

number_list[min_idx], number_list[max_idx] = number_list[max_idx], number_list[min_idx]

# print(min_val)
print(*number_list) # " * " ey symbol er karone list theke comma r first bracket shore jay

