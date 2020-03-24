#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SLLNode:
    def __init__(self, data, pnext = None):
        self.val = data
        self.next = pnext


class SLL:
    def __init__(self):
        self.head = None

    def get_len(self):
        if self.head is None:
            return 0

        current = self.head
        ctr = 0
        while current is not None:
            ctr += 1
            current = current.next
        return ctr

    def print(self):
        curr = self.head
        arr = []
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        print(arr)

    def add_node(self, data, pos=-1):
        # Node that position starts from 1, not 0.
        node = SLLNode(data)
        if pos == -1 and self.head is None:
            pos = 1

        if pos == 1:
            node.next = self.head
            self.head = node
        elif pos == -1:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        else:
            ctr = 1
            current = self.head
            while current is not None and ctr < pos - 1:
                current = current.next
                ctr += 1
            if current:
                node.next = current.next
                current.next = node
            else:
                print("Out of range.")

    def delete_node(self, pos=-1):
        current = self.head
        if current is None:
            print("SLL empty.")
            return
        if pos == -1 and current.next is None:
            pos = 1

        if pos == 1:
            self.head = current.next
            del current
        elif pos == -1:
            while current.next.next is not None:
                current = current.next
            del current.next
            current.next = None
        else:
            ctr = 1
            while current.next is not None and ctr < pos-1:
                current = current.next
                ctr += 1
            if current.next:
                temp = current.next
                current.next = current.next.next
                del temp
            else:
                print("Out of range.")

    def create_from_arr(self, arr):
        for val in arr:
            self.add_node(val)

    def __rev_iter__(self, head):
        prev, curr = None, head
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


class DLLNode:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

            

