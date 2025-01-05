# 一个数组中，数互不相同，求其中和为0的数对的个数
class solution:
    def find_num(self, arr):
        res = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] + arr[j] == 0 and i != j:
                    res += 1
        return res


arr = [1, -1, 4, -4, 5, 6, 3, -7, 0]
S1 = solution()
print(S1.find_num(arr=arr))
