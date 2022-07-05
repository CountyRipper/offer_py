class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #寻找完全平方数
        l,r=0, num//2+1
        while l<r:
            mid = (l+r+1)//2
            if mid*mid == num:
                return True
            elif mid*mid <num:
                l=mid
            else:
                r=mid-1
        return False
s1= Solution()
print(s1.isPerfectSquare(16))
            