t = int(input())

for _ in range(t):
  n = int(input())
  word = input()

  if "aa" in word:
    print(2)
    continue
  elif "aba" in word or "aca" in word:
    print(3)
    continue
  elif "acba" in word or "abac" in word or "acab" in word or "abca" in word:
    print(4)
    continue
  elif "abbaca" in word or "accaba" in word:
    print(6)
    continue
  elif "abbacca" in word or "accabba" in word:
    print(7)
    continue
  else:
    print(-1)
    continue