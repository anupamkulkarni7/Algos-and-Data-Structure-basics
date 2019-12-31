#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:06:29 2019

@author: illuminatus
"""
import random


def partition(arr, li, ri):
    pivot = arr[ri]
    indx = li-1
    for i in range(li, ri):
        if arr[i] <= pivot:
            indx += 1
            arr[indx], arr[i] = arr[i], arr[indx]
    arr[indx+1], arr[ri] = arr[ri], arr[indx+1]
    return indx+1


def quick_sort(arr):

    def sort(arr, li, ri):
        if ri <= li:
            return
        k = random.randint(li,ri)
        arr[ri], arr[k] = arr[k], arr[ri]
        p = partition(arr, li, ri)

        sort(arr, li, p-1)
        sort(arr, p+1, ri)

    sort(arr, 0, len(arr)-1)


def ith_smallest(arr, indx):

    if indx < 0 or indx >= len(arr):
        print("Out of range for array.")
        return

    def helper(arr, li, ri):
        if li >= ri:
            return
        k = random.randint(li, ri)
        arr[ri], arr[k] = arr[k], arr[ri]
        p = partition(arr, li, ri)
        if p == indx:
            return arr[p]
        elif indx < p:
            return helper(arr, li, p-1)
        else:
            return helper(arr, p+1, ri)

    return helper(arr, 0, len(arr)-1)


def merge_sort(arr):

    def merge(arr1, arr2):
        i1 = 0
        i2 = 0
        ans = []
        while i1 < len(arr1) and i2 < len(arr2):
            if arr1[i1] <= arr2[i2]:
                ans.append(arr1[i1])
                i1 += 1
            else:
                ans.append(arr2[i2])
                i2 += 1
        if i1 == len(arr1):
            ans = ans + arr2[i2:]
        if i2 == len(arr2):
            ans = ans + arr1[i1:]
        return ans

    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    a1 = merge_sort(arr[0:mid])
    a2 = merge_sort(arr[mid:])
    return merge(a1, a2)


