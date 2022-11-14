# 合并有序数组
from typing import List
def merge_array(a, b)->List:
    i=0
    j=0
    res=[]
    #len(a)就是m，len(b)就是n
    while i<len(a) and j<len(b):
        if a[i]>=b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[i])
            j+=1
    while i<len(a):
        res.append(a[i])
        i+=1
    while j<len(b):
        res.append(b[j])
        j+=1
    return res
    