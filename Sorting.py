#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:06:29 2019

@author: illuminatus
"""
import random

def partition(arr,li,ri):
    
    pivot = arr[ri]
    indx = li-1
    
    for i in range(li,ri):
        if arr[i]<= pivot:
            indx +=1
            arr[indx],arr[i] = arr[i],arr[indx]
        
    arr[indx+1],arr[ri] = arr[ri],arr[indx+1]
    
    return indx+1



def select(arr,li,ri,K):
    
    if li >= ri: return
    
    k = random.randint(li,ri)
    arr[ri],arr[k] = arr[k],arr[ri]
    
    p = partition(arr,li,ri)
    
    if p == K:
        return
    elif K < p:
        select(arr,li,p-1,K)        
    else:
        select(arr,p+1,ri,K)
    
    return
    

def sort(arr,li,ri):
    
    if li >= ri: return
    k = random.randint(li,ri)
    arr[ri],arr[k] = arr[k],arr[ri]
    
    p = partition(arr,li,ri)
    
    sort(arr,li,p-1)
    sort(arr,p+1,ri)
    return


def kQuickSelect(arr,K):
    #Use recursive quick selection algo to give k smallest entries
    
    select(arr,0,len(arr)-1,K)
    return arr[K]


def QuickSort(arr):
    sort(arr,0,len(arr)-1)


# ---------------------------------------------------

def InsertionSort(arr):
    
    sArr = [0]*len(arr)
    sArr[0] = arr[0]
    
    for i in range(1,len(arr)):
        
        sArr[i] = arr[i]
        for j in range(i-1,-1,-1):
            if sArr[j+1] < sArr[j]:
                sArr[j+1],sArr[j] = sArr[j],sArr[j+1]
            else:
                break
        
    
    return sArr

# ----------------------------------------------------

def mergeSortedArrays(a1,a2):
    
    anew = [0]*(len(a1)+len(a2))
    i1 = 0
    i2 = 0
    
    for i in range(len(a1)+len(a2)):
        if a1[i1] <= a2[i2]:
            anew[i] = a1[i1]
            i1+=1
        else:
            anew[i] = a2[i2]
            i2+=1
        
        if i1 == len(a1):
            anew[i+1:] = a2[i2:]
            break
            
        if i2 == len(a2):
            anew[i+1:] = a1[i1:]
            break

    return anew


def MergeSort(arr):
    
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    s1 = MergeSort(arr[0:mid])
    s2 = MergeSort(arr[mid:])
    
    return mergeSortedArrays(s1,s2)



    
    

    
    