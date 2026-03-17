t = int(input())
for _ in range(t):
    s = input()
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    working_buttns = [char for char, count in char_count.items() if count % 2 == 1]
    print(''.join(sorted(working_buttns)))