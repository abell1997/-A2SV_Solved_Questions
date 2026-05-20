class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        
        for house in houses:
            idx = bisect_right(heaters, house)  
            left_dist = float('inf') if idx == 0 else house - heaters[idx - 1]
            right_dist = float('inf') if idx == len(heaters) else heaters[idx] - house
            ans = max(ans, min(left_dist, right_dist))
        
        return ans