n = int(input())
a = list(map(int, input().split()))

count = 0
while True:
    for x in a:
        if x % 2 != 0:
            print(count)
            exit()
    for i in range(n):
        a[i] = a[i] // 2
    count += 1