class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = 1
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1, col):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[row - 1][col - 1]

    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [0] * col
        dp[0] = 1
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]
        return dp[-1]
