n = input()
nums = list(map(int, input().split()))

freq = {}

for x in nums:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
ans = 0

for x in freq:
    if freq[x] > x:
        ans += freq[x] - x
    elif freq[x] < x:
        ans += freq[x]
print(ans)