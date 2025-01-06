class Solution:
    def pre_sum(self, arr):
        b = [0] * len(arr)
        b[0] = arr[0]
        for i in range(1, len(arr)):
            b[i] = b[i - 1] + arr[i]
        return b


s1 = Solution()
print(s1.pre_sum([1, 2, 3, 4, 5, -1, -5, 3, 6]))
