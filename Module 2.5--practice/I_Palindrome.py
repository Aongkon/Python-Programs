# num = input('the main numbers: ')
num = input()
# num = list(input('here enter the input: '))

# print(num)
# print(num[::-1])

rvs_num1 = num[::-1]
# rvs_num2 = num[::-1]
rvs_num1 = rvs_num1.lstrip('0')

# for n in rvs_num1:
#     if n == '0':
#         rvs_num1 = rvs_num1.replace('0', "")

# print('the rvs_num: ', rvs_num)
print(rvs_num1)

# if rvs_num2 == num:
if rvs_num1 == num:
    print('YES')
else:
    print('NO')


# if normal_num == rvs_num:
#     print(rvs_num)
#     print('YES')
# else:
#     for n in rvs_num:
#         if n == '0':
#             rvs_num.replace(n, " ")
#             print(f'they are numbers of n: {n}')
#         else:
#             print(rvs_num)
#     print('NO')
   