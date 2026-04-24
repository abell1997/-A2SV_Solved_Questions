class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        replacements = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                k = (nums[i] + nums[i+1] - 1) // nums[i+1]
                replacements += k - 1
                nums[i] //= k
        return replacements