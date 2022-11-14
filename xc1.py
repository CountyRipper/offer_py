t = input()
for i in range(int(t)):
    str1, str2 = input().split(" ")
    count = 0
    pos=[]
    for i in range(len(str1)):
        if str1[i]!= str2[i]:
            count=count+1
            pos.append(i)
    if count==0:
        print("Yes")
    elif count!=2:
        print("No")
    else:
        if str1[pos[0]]==str2[pos[1]] and str1[pos[1]]==str2[pos[0]]:
            print("Yes")
        else:
            print("No")