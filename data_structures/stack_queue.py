#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Basic Stacks and Queues:


class MyStack:
    def __init__(self):
        self.data = []
        
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            print("Stack empty.")
    
    def push(self, val):
        return self.data.append(val)
    
    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            print("Stack empty")
            return None
    
    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def print(self):
        print(" {} <-- top ".format(self.data))


class MyQueue:
    def __init__(self):
        self.data = []

    def enq(self, val):
        self.data.append(val)

    def deq(self):
        if not self.is_empty():
            return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if not self.is_empty():
            return self.data[0]

    def size(self):
        return len(self.data)

    def print(self):
        print(" top -->{} ".format(self.data))


# Stacks with specific functions


class StackWMin:
    def __init__(self):
        self.data = []
        self.min = []
    
    def pop(self):
        if len(self.data) > 0:
            self.min.pop()
            return self.data.pop()
            
        else:
            print("Stack empty.")
            return
    
    def push(self, val):
        if len(self.data) == 0:
            self.min.append(val)
            self.data.append(val)
        else:
            self.min.append(min(val,self.min[-1]))
            self.data.append(val)
    
    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            print("Stack empty.")
            return None
    
    def min(self):
        if len(self.data) > 0:
            return self.min[-1]
        else:
            print("Stack empty.")


class SetOfStacks:
    def __init__(self, max_size):
        self.outer_stack = [MyStack()]
        self.max_size = max_size

    def push(self, val):
        if self.outer_stack[-1].size() < self.max_size:
            self.outer_stack[-1].push(val)
        else:
            self.outer_stack.append(MyStack())
            self.outer_stack[-1].push(val)

    def pop(self):
        if not self.outer_stack[-1].is_empty():
            ans = self.outer_stack[-1].pop()
            if self.outer_stack[-1].is_empty() and len(self.outer_stack) > 1:
                self.outer_stack.pop()
            return ans
        else:
            print("Stack empty.")

    def pop_at(self, j):
        if len(self.outer_stack) < j:
            ans = self.outer_stack[j].pop()
            if self.outer_stack[j].is_empty():
                self.outer_stack.pop(j)
            return ans
        else:
            print("Stack is empty at index {}.".format(j))


class QViaStacks:
    def __init__(self):
        self.ss = MyStack()
        self.sq = MyStack()
        self.qmode = False

    def transfer(self, s1, s2):
        while not s1.is_empty():
            s2.push(s1.pop())
        self.qmode = not self.qmode
    
    def enq(self, val):
        if not self.qmode:
            self.ss.push(val)
        else:
            self.transfer(self.sq, self.ss)
            self.ss.push(val)

    def deq_basic(self):
        if not self.sq.is_empty():
            return self.sq.pop()
        else:
            print("Queue is empty.")

    def deq(self):
        if self.qmode:
            return self.deq_basic()
        else:
            self.transfer(self.ss, self.sq)
            return self.deq_basic()
    
    def peek_basic(self):
        if self.sq.is_empty():
            print("Queue is empty.")
        else:
            return self.sq.peek()
    
    def peek(self):
        if self.qmode:
            return self.sq.peek()
        else:
            self.transfer(self.ss, self.sq)
            return self.sq.peek()