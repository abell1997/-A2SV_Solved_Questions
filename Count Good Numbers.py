class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even_positions = (n + 1) // 2  
        odd_positions = n // 2           
        
        count_even = pow(5, even_positions, mod)  
        count_odd = pow(4, odd_positions, mod)    
        
        return (count_even * count_odd) % mod