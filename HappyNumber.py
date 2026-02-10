class Solution:
    def isHappy(self, n: int) -> bool:
        sum = set()
        
        while n != 1 and n not in sum:
            sum.add(n)
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n = n // 10
            n = total
            
        return n == 1


        