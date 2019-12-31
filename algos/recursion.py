#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def power_sets(nums):
    """
    Returns a list of all subsets of the given set nums.
    """
    subsets = []
    if len(nums) == 0:
        return subsets
    pnums = set.copy(nums)
    curr = []

    def helper(pnums, curr):
        if len(pnums) > 0:
            num = pnums.pop()
            curr1 = curr[:]; curr1.append(num)
            pnums1 = set.copy(pnums)

            helper(pnums, curr)
            helper(pnums1, curr1)
        else:
            subsets.append(curr)

    helper(pnums, curr)
    return subsets


def permute_string(input):

    inp = list(input)
    perm = []
    curr = []

    def helper(curr, inp):
        if len(inp) > 1:
            for i in range(len(inp)):
                currnew = curr[:]
                inpnew = inp[:]
                currnew.append(inp[i])
                inpnew.pop(i)
                helper(currnew, inpnew)
        else:
            curr.append(inp[0])
            perm.append(''.join(curr))

    helper(curr, inp)
    return perm

