p=[]
for i in range(12):
    p.append(233*(10**i))

t = input()
for i in range(int(t)):
    num = input()
    n = len(num)
    num = int(num)
    dp=[]
    for t in range(num):
        dp.append(float('inf'))
    dp[0]=0
    for j in p:
        for i in range(j, len(dp)):
            dp[i] = min(dp[i-j]+1,dp[i])
    if dp[num]!=float('inf'):
        print(dp[num])
    else: print(-1)
        