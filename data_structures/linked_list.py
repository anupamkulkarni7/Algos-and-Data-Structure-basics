#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, data, pnext = None):
        self.data = data
        self.next = pnext


class SLL:
    def __init__(self):
        self.head = None
        self.len = 0

    def __setlen__(self):
        if self.head is None:
            self.len = 0

        current = self.head
        ctr = 0
        while current is not None:
            ctr += 1
            current = current.next
        self.len = ctr

    def print_(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def add_node(self, data, pos):
        # Node that position starts from 1, not 0.
        node = ListNode(data)
        if pos == 1:
            node.next = self.head
            self.head = node
            self.len += 1
        elif pos > self.len + 1:
            print("Position larger than linked list length")
        else:
            ctr = 1
            current = self.head
            while current.next is not None and ctr < pos - 1:
                current = current.next
                ctr += 1
            node.next = current.next
            current.next = node
            self.len += 1

    def delete_node(self, pos):
        current = self.head
        prev = None
        if self.len == 0:
            print("SLL empty.")
            return
        if pos == 1:
            self.head = current.next
            self.len -= 1
            del current
            return
        if pos > self.len:
            print("Out of range.")
            return
        ctr = 1
        while current is not None and ctr < pos:
            prev = current
            current = current.next
            ctr += 1
        prev.next = current.next
        self.len -= 1
        del current

    def assign(self, node):
        """
        In cases where we have created a SLL manually by connecting nodes, this assigns 
        such a SLL to the class. Simply stating SLL.head = node requires calling setLen externally,
        this function has been written to package that with assignment. 
        """
        self.head = node
        self.__setlen__()

    def create_sll(self, arr):
        pos = 1
        for val in arr:
            self.add_node(val, pos)
            pos += 1

    def __rev_iter__(self, head):
        curr = head
        prev = None
        nxt = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def __rev_rec__(self, head):
        if head is None or head.next is None:
            return head
        newhead = self.__rev_rec__(head.next)
        head.next.next = head
        head.next = None
        return newhead

    def reverse(self, method='iterative'):
        if method == 'recursive':
            self.head = self.__rev_rec__(self.head)
        else:
            self.head = self.__rev_iter__(self.head)
