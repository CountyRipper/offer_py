# The isBadVersion API is already defined for you.
#def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=0,n
        while l<r:
            mid =(l+r+1)//2
            if isBadVersion(mid):
                #错误
                r=mid-1
            else:
                l=mid
        return l+1