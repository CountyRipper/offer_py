class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = triangle[0][0]
        cur = 0
        for i in range(len(triangle)):
            if cur < len(triangle[i]) and triangle[i][cur] > triangle[i][cur + 1]:
                cur += 1
                res += triangle[i][cur + 1]
            else:
                res += triangle[i][cur]
        return res
