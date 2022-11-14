list1 = input().split()
n = int(list1[0])
max_n = int(list1[1])
list2 = input().split()
dic1 = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,'9':0,'10':0,'J':0,'Q':0,"K":0}
dic2 = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,'9':9,'10':10,'J':11,'Q':12,"K":13}
for i in range(len(list2)):
    dic1[list2[i]]=dic1[list2[i]]+1
three=0
two = 0
four = 0
for key,value in dic1.items():
    if value==3:
        three=three+1
    if value==2:
        two=two+1
    if value==4:
        four=four+1
res = "0,0"
max = 0
if (three+four<1) or(three+four==1 and two<1):
    print(res)
else:
    for k_i,k_v1 in dic1.items():
        for k_j, k_v2 in dic1.items():
            if(k_i!=k_j and k_v1>2 and k_v2>1):
                sum = dic2[k_i]*3+dic2[k_j]*2
                if(sum>max and sum<= max_n):
                    max = sum
                    res = str(dic2[k_i])+" "+str(dic2[k_j])
    print(res)
        
            
    
    
    