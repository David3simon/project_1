#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕'''
def partition(arr,low,high): 
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        # 当前元素小于或等于 pivot 
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    print(i)
    print(arr)
    return ( i+1 ) 
  
 
# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引
  
# 快速排序函数
import time
def quickSort(arr,low,high):
    
    if low < high: 
  
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
    
    
  
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
time1= time.time()
quickSort(arr,0,n-1) 
time2=time.time()
pass_time=time2-time1
print ("排序后的数组:") 
for i in range(n): 
    print ("%d" %arr[i])
print('times: ',pass_time)
