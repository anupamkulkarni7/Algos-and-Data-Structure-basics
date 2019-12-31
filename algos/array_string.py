#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


def is_unique_chars(input, method=1):
    """
    Prob #1.1, CTCI
    Implement an algorithm to determine if a strong has all unique characters.
    What if you cannot use additional data structures?
    """
    if len(input) < 2:
        return True

    if method is 1:
        return len(set(list(input))) == len(input)

    if method is 2:
        print("Warning: Designed considering lowercase ascii strings only.")
        bitvec = 0
        for c in list(input):
            ls = ord(c) - ord('a')
            if bitvec & (1 << ls) is 0:
                bitvec |= (1 << ls)
            else:
                return False
        return True

    if method is 3:
        for i in range(len(input)):
            for j in range(i + 1, len(input)):
                if input[i] is input[j]:
                    return False
        return True

    if method is 4:
        sinp = sorted(input)
        for i in range(1,len(sinp)):
            if sinp[i-1] is sinp[i]:
                return False
        return True


def is_permutation(s1, s2, method=1):
    """
    Prob #1.2, CTCI
    """
    if method is 1:
        return Counter(list(s1)) == Counter(list(s2))

    if method is 2:
        return sorted(s1) == sorted(s2)


def urlify(s, method=1):
    """
    Prob #1.3, CTCI
    Write a method to replace all spaces in the input string with '%20'.
    """
    if method is 1:
        return '%20'.join(s.split())


def is_palindrome_perm(s, method=1):
    """
    Prob #1.4, CTCI
    Given a string, write a function to check if it is a permutation of a palindrome.
    """
    sf = ''.join(s.lower().split())
    if method is 1:
        ref = Counter(list(sf))
        count = len(ref.keys()) - sum([int((ref[c]/2).is_integer()) for c in ref.keys()])
        if count > 1:
            return False
        else:
            return True

    if method is 2:
        count = set()
        for c in list(sf):
            if c in count:
                count.remove(c)
            else:
                count.add(c)

        if len(count) > 1:
            return False
        else:
            return True


def one_away(s1, s2, method=1):
    """
    Prob #1.5, CTCI
    There are 3 types of edits that can be performed in a string: insert/remove/replace a character.
    Given 2 strings, write a function to check if they are 1 (or 0) edits away from each other.
    """
    def one_replace(s1, s2):
        cnt = sum([int(c1 is not c2) for c1, c2 in zip(list(s1), list(s2))])
        if cnt > 1:
            return False
        else:
            return True

    def one_insert(short, long):
        for i in range(len(short)):
            if short[i] is not long[i]:
                return short[i:] == long[i+1:]
        return True

    if method is 1:
        if len(s1) == len(s2):
            return one_replace(s1, s2)
        elif abs(len(s1) - len(s2)) > 1:
            return False
        else:
            if len(s1) > len(s2):
                return one_insert(s2, s1)
            else:
                return one_insert(s1, s2)


def string_compress(s):
    """
    Prob #1.6, CTCI
    Given a string, compress it using counts of repeated characters, for ex. aaddddfeaa = a2d4f1e1a2.
    If resultant string is longer, return original.
    """
    if len(s) < 3:
        return s

    cnt = [s[0]]
    count = 1
    for i in range(1, len(s)):
        if s[i] == cnt[-1]:
            count += 1
        else:
            cnt.append(str(count))
            cnt.append(s[i])
            count = 1
    cnt.append(str(count))
    cs = ''.join(cnt)
    if len(cs) < len(s):
        return cs
    else:
        return s




