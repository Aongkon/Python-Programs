a, b = map(int, input().split())
# lucky = " " space also a character
lucky = ""
is_lucky = True
for n in range(a, b+1):
    for x in str(n):
        is_lucky = True
        if x != '4' and x != '7':
            is_lucky = False
            break
    if is_lucky:
        lucky += str(n) + " "

if lucky: #lucky string er moddhe jdi kicho thake tobe print korbe
    print(lucky)
else:
    print('-1')