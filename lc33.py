class Solution(object):
    def search(self, nums, target):
        l,r = 0, len(nums)-1
        while l<r :
            mid = (l+r+1)//2
            if nums[l]<nums[mid]:
                #如果前面的有序
                l=mid
            else:
                #如果是后面有序
                r=mid-1
        if(len(nums)==1):
            return 0 if nums[0]==target else -1
        #两种情况，一种是无旋转，正常二分，一种是有旋转，先判断
        l1,r1=0,len(nums)-1
        if l==len(nums)-1:
            #无旋转
            if(target<nums[0] or target>nums[-1]):
                return -1
        else:
            #有旋转
            if target<nums[l+1] or target>nums[l]:
                return -1
            else:
                if target<nums[0]:
                    l1=l+1
                else:
                    r1=l
        while l1<r1:
            mid=(r1+l1+1)//2
            if nums[mid]<target:
                l1=mid
            elif nums[mid]>target:
                r1=mid-1
            else:
                return mid
        if nums[l1]==target:
            return l1
        return -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
s1 = Solution()
list=[1,3]
target = 3
print(s1.search(list,target))