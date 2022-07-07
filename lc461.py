class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #先异或xor，再算有多少1
        res = x^y
        n=0
        while res!=0:
            res&=(res-1)
            n+=1
        return n
