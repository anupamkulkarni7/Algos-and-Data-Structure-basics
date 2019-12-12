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
        return
        
    def has_value(self,value):
        return self.data == value

#-----------------------------------

class SLL:
    
    def __init__(self):
        self.head = None
        self.len = 0

#   -------------------------
    def __setLen__(self):
        
        if self.head == None:
            self.len = 0
            return
        
        current = self.head
        ctr = 0
        while current != None:
            ctr +=1
            current = current.next
        
        self.len = ctr
        return
#   -------------------------
        
    def print_(self):
        
        pval = self.head
        while pval is not None:
            print(pval.data)
            pval = pval.next
 
#   -------------------------    
    
    def addNode(self,node,pos):
    #Node that position starts from 1, not 0. 
    
        if pos == 1:
            node.next = self.head
            self.head = node
            self.len += 1
            return
        
        if pos > self.len+1:
            print("Position larger than linked list length")
            return
        
        ctr = 1
        current = self.head
        while current.next is not None and ctr < pos-1:
            current = current.next
            ctr += 1
        
        node.next = current.next
        current.next = node
        self.len +=1
        return
    
#   -------------------------
    def deleteNode(self,pos):
        
        current = self.head
        prev = None
        
        if self.len == 0:
            print ("SLL empty.")
            return 
        
        if self.len == 1:
            del(current)
            self.head = None
            self.len = 0
            return
        
        if pos == 1:
            self.head = current.next
            self.len -= 1
            del(current)
            return
        
        if pos>self.len:
            print("LL too short. ")
            return
        
        ctr = 1
        while current != None and ctr<pos:
            prev = current
            current = current.next
            ctr +=1
        
        prev.next = current.next
        del(current)
            
    
#   -------------------------
    def assign(self,node):
        """
        In cases where we have created a SLL manually by connecting nodes, this assigns 
        such a SLL to the class. Simply stating SLL.head = node requires calling setLen externally,
        this function has been written to package that with assignment. 
        """
        self.head = node
        self.__setLen__()
        return 
        
#   -------------------------

def reverseSLLRec(head):
        
    if head is None:
        return None
        
    if head.next == None:
        return head
        
    temp = reverseSLLRec(head.next)
    head.next.next = head
    head.next = None
        
    return temp

def reverseSLL(head):
    
    if head is None:
        return None
    
    if head.next is None:
        return head
    
    current = head
    temp1 = None
    temp2 = None
    
    while current!= None:
        temp2 = current.next
        current.next = temp1
        temp1 = current
        current = temp2
    
    return temp1
        
 
def main():
    n1 = Node(1); n2=Node(2); n3 = Node(3)
    SLL1=SLL()
    #SLL1.addNode(n1,1)
    #SLL1.addNode(n2,2)
    #SLL1.addNode(n3,3)
    
    n1.next = n2; n2.next=n3; n3.next=Node(4)
    SLL1.assign(n1)
    print("Len:", SLL1.len)
    #SLL1.deleteNode(3)
    SLL1.print_()
    SLL1.head = reverseSLLRec(SLL1.head)
    SLL1.print_()
    SLL1.head = reverseSLL(SLL1.head)
    SLL1.print_()
    
    
if __name__ == '__main__':
    main()
    
    