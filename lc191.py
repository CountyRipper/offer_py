class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n>0:
            n&=(n-1)
            res+=1
        return res
s1 = Solution()
print(s1.hammingWeight(0b11111111111111111111111111111101))