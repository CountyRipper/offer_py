class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)-1
        res=''
        for i in range(len(s)):
            tmp=''
            for j in range(min(i,n-i)+1):
                if s[i-j]==s[i+j]:
                    if i-j==i+j:
                        tmp+=s[i-j]
                    else:
                        tmp=s[i-j]+tmp+s[i+j]
                else:
                    break
            if len(tmp)>len(res):
                res=tmp
        return res
s1 = Solution()
str='cbbd'
print(s1.longestPalindrome(str))