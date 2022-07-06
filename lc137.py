from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a,b=0,0
        for i in nums:
            #两个变量同时赋值
            a,b= (~a&b&i)|(a&~b&~i), ~a&(b^i)
            #非同时赋值需要改写真值表
            # b= ~a(b^i)
            # a= ~b(a^i)
        return b