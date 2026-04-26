class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bucks = 0
        ten_bucks = 0
        
        for bill in bills:
            if bill == 5:
                five_bucks += 1
            elif bill == 10:
                if five_bucks == 0:
                    return False
                five_bucks -= 1
                ten_bucks += 1
                
            else:
                if ten_bucks > 0 and five_bucks > 0:
                    ten_bucks -= 1
                    five_bucks -= 1
                elif five_bucks >= 3:
                    five_bucks -= 3
                else:
                    return False
        
        return True