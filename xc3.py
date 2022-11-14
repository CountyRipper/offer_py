n,k = input().split(" ")
n=int(n) 
k = int(k)

nums = [int(i) for i in input().split(" ")]
nums.sort()
k1 = int(k//2)
k2=0
if k%2!=0:
    k2=1
l = len(nums)-1
avg=0
for i in range(k1):
    avg = avg+(nums[i]+nums[l-i])
avg=avg/k

for i in range(k1):
    nums[i]=avg
    nums[l-i]=avg
nums.sort()
print(nums[-1]-nums[0])
