t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    red_sumMax = 0
    current_red_sum = 0
    for num in r:
        current_red_sum += num
        red_sumMax = max(red_sumMax, current_red_sum)

    blue_sumMax = 0
    current_blue_sum = 0
    for num in b:
        current_blue_sum += num
        blue_sumMax = max(blue_sumMax, current_blue_sum)

    print(red_sumMax + blue_sumMax)