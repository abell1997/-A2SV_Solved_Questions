class Solution:
        def splitString(self, s: str) -> bool: 
            def rec(start , parts , prev):
                if start == len(s):
                    return parts >= 2

                for i in range(start , len(s)):
                    num = int(s[start : i + 1])

                    if prev == -10000 or num == prev - 1:
                        if rec(i+1 , parts+1 , num):
                            return True
                
                return False
            return rec(0 , 0 , -10000) 
                  