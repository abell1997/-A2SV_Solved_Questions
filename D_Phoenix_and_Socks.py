
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    colors = list(map(int, input().split()))

    left_colors = {}
    right_colors = {}

    for i in range(l):
        left_colors[colors[i]] = left_colors.get(colors[i], 0) + 1

    for i in range(l, n):
        right_colors[colors[i]] = right_colors.get(colors[i], 0) + 1

    pairs = 0
    for color in left_colors:
        if color in right_colors:
            pairs += min(left_colors[color], right_colors[color])

    unmatched_left = l - pairs
    unmatched_right = r - pairs

    cost = 0
    if unmatched_left > unmatched_right:
        cost += (unmatched_left - unmatched_right) // 2
        cost += unmatched_right + (unmatched_left - unmatched_right) // 2
    else:
        cost += (unmatched_right - unmatched_left) // 2
        cost += unmatched_left + (unmatched_right - unmatched_left) // 2

    print(cost)

