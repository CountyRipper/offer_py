class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = matrix[-1][:]

        for i in range(n - 2, -1, -1):
            t_dp = [0] * n
            for j in range(n):
                min_sum = dp[j]
                if j > 0:
                    min_sum = min(min_sum, dp[j - 1])
                if j < n - 1:
                    min_sum = min(min_sum, dp[j + 1])
                # 上一层更新最小值
                t_dp[j] = matrix[i][j] + min_sum
            dp = t_dp
        return dp[-1]
