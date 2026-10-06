s = input()

start = 0
count = 0
ans = []

for i in range(len(s)):
    if s[i] == 'L':
        count = count - 1
    else:
        count = count + 1

    if count == 0:
        ans.append(s[start : i+1])
        start = i+1

print(len(ans))
for seq in ans:
    print(seq)
