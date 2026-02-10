class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        separated_digits = []

        for num in nums:
            for digit in str(num):
                separated_digits.append(int(digit))
        return separated_digits
        