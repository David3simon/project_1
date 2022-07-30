#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，
一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端'''
import time
def bubbleSort(arr):
    
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    
arr = [10, 7, 8, 9, 1, 5]
time1=time.time() 
bubbleSort(arr)
time2=time.time()
pass_time=time2-time1 
print ("排序后的数组:")
for i in range(len(arr)):
    print ("%d" %arr[i])
print('times: ',pass_time)