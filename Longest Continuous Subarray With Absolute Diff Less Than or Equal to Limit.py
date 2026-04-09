class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
     left = 0
     ans = 0
     n = len(nums)
     _max = []
     _min = []

     for right in range(n):
        while _max and nums[_max[-1]] <= nums[right]:
            _max.pop()
        while _min and nums [_min[-1]] >= nums[right]:
            _min.pop()
        
        _max.append(right)
        _min.append(right)

        while nums[_max[0]] - nums[_min[0]] > limit:
            left += 1
            if _max[0] < left:
                _max.pop(0)
            if _min[0] < left:
                _min.pop(0)
        
        ans = max(ans, right - left+1)

     return ans