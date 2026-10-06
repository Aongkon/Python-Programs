n = int(input())
new_list = list(map(int, input().split()))

rev_new_list = new_list[::-1]

if new_list == rev_new_list:
    print('YES')
else:
    print('NO')