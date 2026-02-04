#Geeks for Geeks

class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
        
        freq_map = {}
        
        for num in a:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num in b:
            if num not in freq_map or freq_map[num] == 0:
                return False
            freq_map[num] -= 1
        
        return True