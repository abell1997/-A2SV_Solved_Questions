class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        score_diff = [[0] * n for _ in range(n)]
        for i in range(n):
            score_diff[i][i] = nums[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                score_diff[i][j] = max(nums[i] - score_diff[i + 1][j], nums[j] - score_diff[i][j - 1])
        return score_diff[0][n - 1] >= 0