class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    # 贪心思想: 从下往上，最后一行的最小值解，肯定是上一行紧邻的三个位置的最小下降路径长度最小解+当前坐标的和
    # dp[i][j]= matrix[i][j]+ min(dp[i-1][j],dp[i-1])[j-1],dp[i-1][j+1]
    n = len(matrix)
    dp [[0]*n for i in range(len(matrix))]

    for i
