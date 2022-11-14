# @param a string字符串 字符串1
# @param b string字符串 字符串2
# @return int整型

class Solution:
    def minDistance(self , a , b ):
        al = len(a)
        bl = len(b)
        dp=[]
        for i in range(al+1):
            dp.append([0]*(bl+1))
        for i in range(1,al+1):
            dp[i][0]=i
        for i in range(1,bl+1):
            dp[0][i]=i
        for i in range(1,al+1):
            for j in range(1,bl+1):
                if a[i-1] == b[j-1]:
                    #相等
                    dp[i][j]=dp[i-1][j-1]
                else:
                    #不相等情况 插入，删除，更改
                    dp[i][j] = 1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        return dp[al][bl]
    