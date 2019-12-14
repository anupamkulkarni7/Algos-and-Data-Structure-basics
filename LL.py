#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 15:53:35 2019

@author: illuminatus
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.len = 0

    def __setLen__(self):
        if self.head == None:
            self.len = 0

        current = self.head
        ctr = 0
        while current != None:
            ctr += 1
            current = current.next
        self.len = ctr

    def print_(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def addNode(self, data, pos):
        # Node that position starts from 1, not 0.
        node = Node(data)
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

    def deleteNode(self, pos):
        current = self.head
        prev = None
        if self.len == 0:
            print("SLL empty.")

        if self.len == 1:
            del current
            self.head = None
            self.len = 0

        if pos == 1:
            self.head = current.next
            self.len -= 1
            del current

        if pos > self.len:
            print("LL too short. ")

        ctr = 1
        while current is not None and ctr < pos:
            prev = current
            current = current.next
            ctr += 1
        prev.next = current.next
        del current

    def assign(self, node):
        """
        In cases where we have created a SLL manually by connecting nodes, this assigns 
        such a SLL to the class. Simply stating SLL.head = node requires calling setLen externally,
        this function has been written to package that with assignment. 
        """
        self.head = node
        self.__setLen__()

    def createSLL(self, arr):
        pos = 1
        for val in arr:
            self.addNode(val, pos)
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


def main():
    n1 = Node(1); n2 = Node(2); n3 = Node(3)
    SLL1 = SLL()
    # SLL1.addNode(n1,1)
    # SLL1.addNode(n2,2)
    # SLL1.addNode(n3,3)

    n1.next = n2;
    n2.next = n3;
    n3.next = Node(4)
    SLL1.assign(n1)
    print("Len:", SLL1.len)
    # SLL1.deleteNode(3)
    SLL1.print_()
    SLL1.head = reverseSLLRec(SLL1.head)
    SLL1.print_()
    SLL1.head = reverseSLL(SLL1.head)
    SLL1.print_()


if __name__ == '__main__':
    main()
