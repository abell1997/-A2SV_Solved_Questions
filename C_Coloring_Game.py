import sys
from bisect import bisect_right

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        a.sort()
        
        ans = 0
        max_val = a[-1]
        
        for i in range(n):
            a_i = a[i]
            target_base = max(a_i, max_val - a_i)
            
            for j in range(i):
                a_j = a[j]
                threshold = target_base - a_j
                
                k = bisect_right(a, threshold, 0, j)
                ans += (j - k)
                
        out.append(str(ans))
        
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()