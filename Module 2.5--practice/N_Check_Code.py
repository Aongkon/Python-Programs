a, b = map(int, input().split())
s = input()

if len(s) != a+b+1:
    print('No')
elif s[a] != '-':
    print('No')
else:
    ok = True
    for i in range(len(s)):
        if i == a:
            continue

        if not s[i].isdigit():
            ok = False
            break
    if ok:
        print('Yes')
    else:
        print('No')