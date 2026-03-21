import sys
input = sys.stdin.readline

t = int(input())

for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    res = [a[0]]
    for i in range(1, n - 1):
        if (a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1]):
            res.append(a[i])
    res.append(a[-1])
    
    print(len(res))
    print(*res)