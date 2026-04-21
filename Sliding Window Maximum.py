class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        result = []
        deque = collections.deque()
        
        for i in range(len(nums)):
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            
            if deque[0] == i - k:
                deque.popleft()
            if i >= k - 1:
                result.append(nums[deque[0]])
                
        return result