#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Chapter 2: Linked Lists


from data_structures.linked_list import *


def remove_duplicates(sll):
    """
    Prob #2.1, CTCI
    """


def numberSumReverse(c1, c2, carry):
    
    if c1 == None and c2== None and carry ==0:
        return None
        
    if c1 == None and c2 == None:
        nn = Node(carry)
        nn.next = None
        return nn
    
    if c1 == None:
        val = (c2.data + carry)%10
        newcarry = int((c2.data + carry)/10)
        nn = Node(val)
        nn.next = numberSumReverse(None,c2.next,newcarry)
        return nn
    
    if c2 == None:
        val = (c1.data + carry)%10
        newcarry = int((c1.data + carry)/10)
        nn = Node(val)
        nn.next = numberSumReverse(c1.next,None,newcarry)
        return nn
    
    val = (c1.data + c2.data + carry)%10
    newcarry = int((c1.data + c2.data + carry)/10)
    nn = Node(val)
    nn.next = numberSumReverse(c1.next,c2.next,newcarry)
    return nn

    

def testR(list1,list2):
    
    SLL1 = SLL()
    SLL2 = SLL()
    
    for i,val in enumerate(list1):
        node = Node(val)
        SLL1.addNode(node,i+1)
    
    for i,val in enumerate(list2):
        node = Node(val)
        SLL2.addNode(node,i+1)
    
    SLLsum = SLL()
    SLLsum.head = numberSumReverse(SLL1.head, SLL2.head, 0)
    SLLsum.setLen()
    print('SLL Length',SLLsum.len)
    SLLsum.SLLprint()

#   -------------------------------------------------------- 
    

def numberSumLL(node1,node2):
    
    print(node1.data,node2.data)
    
    if node1.next == None and node2.next == None:
        val = (node1.data + node2.data)%10
        carry = int((node1.data + node2.data)/10)
        nn = Node(val)
        nn.next = None
        return nn, carry
    
    nn = Node(0)
    nn.next, carry = numberSumLL(node1.next,node2.next)    
    nn.data = (node1.data + node2.data + carry)%10
    newcarry = int((node1.data + node2.data + carry)/10)
    
    return nn,newcarry

   
def correctLens(SLL1,SLL2):
    
    padl = SLL1.len - SLL2.len
    
    if padl > 0:
        for i in range(padl):
            SLL2.addNode(Node(0),1)
    else:
        for i in range(abs(padl)):
            SLL1.addNode(Node(0),1)
    
    
    
def testF(list1,list2):
    
    SLL1 = SLL()
    SLL2 = SLL()
    
    for i,val in enumerate(list1):
        node = Node(val)
        SLL1.addNode(node,i+1)
    
    for i,val in enumerate(list2):
        node = Node(val)
        SLL2.addNode(node,i+1)
        
    
    if SLL1.len != SLL2.len:
        correctLens(SLL1,SLL2)
    
    
    SLLs = SLL()
    SLLs.head,carry = numberSumLL(SLL1.head,SLL2.head)
    
    if carry >0:
        SLLs.addNode(Node(carry),1)
    
    SLLs.SLLprint()
#   -------------------------------------------------------- 
        
    
    

def main():
    
    a = [9,2,6,2,3] 
    b = [3,4,5]
    
    testF(a,b)
    
    
if __name__ == '__main__':
    main()
    
    
    

