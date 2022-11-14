t = int(input())
for i in range(t):
    nums=[int(i) for i in input().split(" ")]
    flag = False
    for j in range(len(nums)-1,0,-1):
        pre=0
        end=j
        sum1=0
        for k in range(j-1):
            sum1+=nums[k]
        
        