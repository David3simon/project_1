#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，
对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入'''
import time
def insertionSort(arr): 
    
    
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
    
    
  
  
arr = [10, 7, 8, 9, 1, 5] 
time1=time.time()
for i in range(10000):
    insertionSort(arr) 
time2=time.time()
pass_time=(time2-time1)/10000
print ("排序后的数组:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])
print('times: ',pass_time)