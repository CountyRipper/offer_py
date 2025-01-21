class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #给定一个字符串s，找出最长的回文子序列，并返回该序列长度
        def dfs(i:int , j: int) ->int:
            if i >j:
                return 0 # 空串返回，递归结束条件
            if i==j:
                return 1 #仅有一个字母时
            if s[i] == s[j]:
                return dfs(i+1,j-1)+2
            return max(dfs(i+1,j),dfs(i,j-1)) #枚举选最大的
        
        return dfs(0,len(s)-1)
        
    def longestPalindromeSubseq_dp(self,s:str) -> int:

