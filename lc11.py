# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0
        right = 0
        left = len(height) - 1
        vol = abs(left - right) * min(height[left], height[right])
        while right < left:
            if height[right] >= height[left]:
                left -= 1
            else:
                right += 1
            if vol < abs(left - right) * min(height[left], height[right]):
                vol = abs(left - right) * min(height[left], height[right])
        return vol
