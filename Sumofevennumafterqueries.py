class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for x in nums:
            if x % 2 == 0:
                evenSum += x
        result = []
        for val, index in queries:
            if nums[index] % 2 == 0:
                evenSum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                evenSum += nums[index]
            result.append(evenSum)
        return result
