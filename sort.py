# python实现排序算法
# 1. 冒泡排序
# 2. 选择排序
# 3. 插入排序
# 4. 希尔排序
# 5. 归并排序
# 6. 快速排序
# 7. 堆排序
from typing import List
import numpy as np
import math
def bubble_sort(list_1:List)->List:
    n = len(list_1)
    for i in range(n):
        for j in range(n-i-1):
            if list_1[j]>list_1[j+1]:
                tmp = list_1[j]
                list_1[j] = list_1[j+1]
                list_1[j+1] = tmp
    return list_1

def select_sort(list_1:List)->List:
    n = len(list_1)
    #max_n = list_1[0]
    for i in range(n):
        min_idx = i
        for j in range(i,n):
            if list_1[j]<list_1[min_idx]:
                min_idx = j
        tmp = list_1[i]
        list_1[i] = list_1[min_idx]
        list_1[min_idx] = tmp
    return list_1
'''
插入排序：外环从1开始而不是0，取第一个不有序的值，从头开始或者从尾部开始都可以，这里是从头部开始，
内环是从一个有序的列表中从后往前遍历，如果发现更大的值，就把当前的数组的值往后移一位，
由于每次取出来的值的idx是不断变大的，所以整个有序数组从头往后扩张
'''
def insert_sort(list_1:List)-> List:
    n = len(list_1)
    for i in range(1,n):
        j = i-1
        tmp = list_1[i]
        while list_1[j]>tmp and j>=0:
            list_1[j+1] = list_1[j]
            j -=1
        list_1[j+1] = tmp    
    return n_list        
n_list = np.random.randint(-1000, 1000, 10).tolist()
print(n_list)
print(insert_sort(n_list))