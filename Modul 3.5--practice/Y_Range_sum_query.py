n, q = map(int, input().split())
nums = list(map(int, input().split()))

while q:
    l, r = map(int, input().split())

    total = 0
    for i in range(l-1, r):
        total += nums[i]

    print(total)

    q -= 1