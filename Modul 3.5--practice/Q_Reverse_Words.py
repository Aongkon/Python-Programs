# s = input()

# words = s.split()
# for word in words:
#     print(word[::-1], end=" ")

#//
s = input()
words = s.split()

ans = []
for word in words:
    ans.append(word[::-1])
print(*ans)