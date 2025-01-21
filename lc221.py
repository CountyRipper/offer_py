class Solution:
    # 我们用 dp(i,j) 表示以 (i,j) 为右下角，且只包含 1 的正方形的边长最大值。
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp(i,j)
        row = len(matrix)
        col = len(matrix[0])

        dp = [[0] * col for _ in range(row)]
        max_side = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
