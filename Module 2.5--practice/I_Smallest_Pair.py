t = int(input())

while t:
    ans = float('inf') #shobcheye boro shongkha ke bojhay
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(0, n):
        for j in range(i+1, n):
            res = a[i] - i + a[j] + j
            if res < ans:
                ans = res
    print(ans)
    t = t - 1
