l_list = input().split()
list = list(map(int,l_list))
tmp = list[1:]
m = 0
tmps = []
while m< len(tmp):
    cur = []
    if tmp[m]>= -10 and tmp[m]<=30:
        while m<len(tmp):
            cur.append(tmp[m])
            m=m+1
        tmps.append(cur)
    else:
        m=m+1
long_tmp = 0
cur_tmp=[]
curr=0
for i in range(len(tmps)):
    if long_tmp<len(tmps[i]):
        long_tmp=len(tmps[i])
        curr=i
cur_tmp=tmps[i]
if list[0]!=0:
    
    n=1
    count = 0
    day=0
    flag = 1
    while cur_tmp[count]< -10 and count <len(cur_tmp):
        count=count+1
    while count<len(cur_tmp):
        if cur_tmp[count]>= -10 and cur_tmp[count]<= 30:
            n=n+n
            day=day+1
            count=count+1
        else:
            if n>4:
                n=n/2
                if n<=4:
                    flag = 0
                    break
                n=n/2
                day=day+1
                count=count+1
            else:
                flag = 0
                break            
    if flag:
        #说明不是死亡情况：
        day=day-1
    print(day)
else:
    print(0)
