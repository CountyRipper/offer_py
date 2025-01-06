class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0] * (n + 1)
        if n > 0:
            arr[1] = 1
        if n > 1:
            arr[2] = 1
        if n > 2:
            for i in range(3, n + 1):
                arr[i] = arr[i - 3] + arr[i - 1] + arr[i - 2]
        return arr[n]
