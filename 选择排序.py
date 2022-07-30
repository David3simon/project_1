#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
'''选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中
找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕'''
import time
A = [10, 7, 8, 9, 1, 5]
def main(): 
      
    for i in range(len(A)): 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j             
        A[i], A[min_idx] = A[min_idx], A[i] 
    
    
time1= time.time()
main()
time2= time.time()  
pass_time=time2-time1
print ("排序后的数组：") 
for i in range(len(A)): 
    print("%d" %A[i])
print('times: ',pass_time)
