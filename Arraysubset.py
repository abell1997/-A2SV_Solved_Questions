#GeeksforGeeks

class Solution:
    def isSubset(self, a, b):
        set_a = set(a)
        set_b = set(b)
        
        for element in set_b:
            if element not in set_a:
                return False
        return True