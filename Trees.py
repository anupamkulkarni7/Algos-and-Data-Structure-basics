#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:31:55 2019

@author: illuminatus
"""

"""
Given a sorted int array (increasing order), create a BST with min depth
"""

import queue
from SnQ import *

class TreeNode:
    
    def __init__(self,val):
        self.val = val
        self.lc = None
        self.rc = None


class Tree:
    
    def __init__(self):
        self.root = None

#   -----------------------------------

    def BFS(self):
        
        q = queue.Queue()
        q.put(self.root)
        nlist = [self.root]
        plist = [self.root]
        dlist = {self.root:0}
        
        while not q.empty():
            node = q.get()
            print(node.val,dlist[node])
            if node.lc:
                q.put(node.lc)
                nlist.append(node.lc)
                plist.append(node)
                dlist[node.lc] = dlist[node] + 1
            if node.rc:
                q.put(node.rc)
                nlist.append(node.rc)
                plist.append(node)
                dlist[node.rc] = dlist[node] + 1
    
        return nlist,plist
#   -----------------------------------
                
    def __trecs__(self,node,level,method,func):
        
        if method == 'preorder':
            if node:
                func(node,level)
                self.__trecs__(node.lc,level+1,method,func)
                self.__trecs__(node.rc,level+1,method,func)
                
        elif method == 'inorder':
            if node:
                self.__trecs__(node.lc,level+1,method,func)
                func(node)
                self.__trecs__(node.rc,level+1,method,func)
                
        elif method == 'postorder':
            if node:
                self.__trecs__(node.lc,level+1,method,func)
                self.__trecs__(node.rc,level+1,method,func)
                func(node)
        
        else:
            print('Wrong method chosen.')
        
        return
    
    
    def traverseRec(self,method='preorder',func=lambda x: print(x.val)):
        
        node = self.root
        self.__trecs__(node,0,method=method,func=func)
        
        return
    
#   -----------------------------------
        
    def traverseIter(self, method='preorder'):
        
        s = myStack()
        
        if method == 'preorder':
            s.push(self.root)

            while s.size() > 0:
            
                node = s.pop()
                print(node.val)
            
                if node.rc is not None:
                    s.push(node.rc)
            
                if node.lc is not None:
                    s.push(node.lc)
        
        elif method == 'inorder':
            s.push(self.root)
            while s.size()>0:
                
                node = s.pop()
                if node is not None:
                    s.push(node.rc)
                    s.push(node)
                    s.push(node.lc)
                else:
                    if s.size()>0:
                        print(s.pop().val)
                    
        elif method == 'postorder': #post order
            
            s.push(self.root)
            
            
            while s.size()>0:
                
                node = s.pop()
                if node is not None:
                    s.push(node)
                    s.push(node.rc)
                    s.push(node.lc)
                else:
                    if s.top() is not None:
                        node = s.pop()
                        s.push(None)
                        s.push(node)
                    else:
                        _ = s.pop()
                        node = s.pop()
                        print(node.val)
                        if s.size() > 0:
                            s.push(None)
        else:
            print('Incorrect method specified.')
            
#   ---------------------------------------

    #def DFS(self):
        
            
#   ---------------------------------------------------------------------------


class BST(Tree):
    
    def __init__(self):
        self.root = None
        
    def addNode(self,val):
        
        node = TreeNode(val)
        current = self.root
        
        if current is None:
            self.root = node
            return
        
        while 1:
            
            #right branch
            if val > current.val:
                if current.rc:
                    current = current.rc
                else:
                    current.rc = node
                    break
                
            #left branch
            if val < current.val:
                if current.lc:
                    current = current.lc
                else:
                    current.lc = node
                    break
        
        return
    
    
    
#Tree creators
def BSTFromSortedArr(arr,idxs,idxe):
    
    if idxs > idxe:
        return None
    
    
    mid = int((idxe+idxs)/2)
    node = TreeNode(arr[mid])
    
    
    node.lc = BSTFromSortedArr(arr,idxs,mid-1)
    node.rc = BSTFromSortedArr(arr,mid+1,idxe)
    
    return node


def BSTfromArr(arr):
    tree = BST()
    
    for val in arr:
        tree.addNode(val)
    
    return tree



def coolBSTree1():
    tree = BST()
    tree.addNode(20)
    tree.addNode(10); tree.addNode(30)
    tree.addNode(5); tree.addNode(15) #;tree.addNode(10); tree.addNode(14)
    #tree.addNode(3); tree.addNode(9)
    tree.addNode(3);tree.addNode(7); tree.addNode(17)
    
    
    return tree
    


def Btree2Node():
    #pg 258
    tree = Tree()
    node = TreeNode(20); tree.root = node
    node.lc = TreeNode(10); node.rc = TreeNode(30)
    node = node.lc; node.lc = TreeNode(5); node.rc = TreeNode(15)
    node.lc.lc = TreeNode(3); node.lc.rc = TreeNode(7)
    node.rc.rc = TreeNode(17)
    
    return tree, tree.root.lc.lc.rc, node.rc.rc

#   ---------------------------------------------------------------------------

def lvlprint(x,level):
    print (x.val,level)


def getNodeHeight(node):
    
    if node is None:
        return -1
    
    return max(getNodeHeight(node.lc),getNodeHeight(node.rc)) + 1


def isBalanced1(node):
    
    if node is None:
        return True
    
    hdiff = abs(getNodeHeight(node.lc) - getNodeHeight(node.rc))
    if hdiff>1:
        return False
    else:
        return isBalanced1(node.lc) and isBalanced1(node.rc)


def checkHeight(node):

    if node is None:
        return -1
    
    left = checkHeight(node.lc)
    if left is None:
        return None
    
    right = checkHeight(node.rc)
    if right is None:
        return None
    
    diff = abs(left - right)
    
    if diff>1:
        return None
    else:
        return max(left,right) + 1

def isBalanced2(node):
    return checkHeight(node) != None
    



def isBST(node, minkey, maxkey):
    
    if node is None:
        return True
    
    if (minkey is not None and node.val<= minkey) or (maxkey is not None and node.val>maxkey):
        return False
        
    if not isBST(node.lc,minkey,node.val) or not isBST(node.rc,node.val,maxkey):
        return False
    
    return True




def isNodeinTree(node,root):
    
    if root is None:
        return False
    
    if node == root:
        return True
    
    return isNodeinTree(node,root.lc) or isNodeinTree(node,root.rc)


def CommonAncestor1(root,tn1,tn2):
    
    current = root
    while 1:
        if current is None or current is tn1 or current is tn2:
            return current
        
        lside = isNodeinTree(tn1,current.lc) or isNodeinTree(tn2,current.lc)
        rside = isNodeinTree(tn1,current.rc) or isNodeinTree(tn2,current.rc)
        
        if lside is True and rside is True:
            return current
        
        if lside is True:
            current = current.lc
        elif rside is True:
            current = current.rc
        else:
            return None
        


def AncestorHelp(root,tn1,tn2):
    
    if root is None:
        return None

    if root is tn1 or root is tn2:
        return root
    
    left = AncestorHelp(root.lc,tn1,tn2)        
    right = AncestorHelp(root.rc,tn1,tn2)

    if left is None and right is None:
        return None
    
    if left is None:
        return right
    
    if right is None:
        return left
    
    return root
    
    

def CommonAncestor2(root,tn1,tn2):
    
    if isNodeinTree(tn1,root) and isNodeinTree(tn2,root):
        return AncestorHelp(root,tn1,tn2)
    else:
        return None

#   ---------------------------------------------------------------------------   

def main():
    """
    arr = list(range(1,16))
    tree = Tree()
    tree.root = BSTFromSortedArr(arr,0,len(arr)-1)
    tree.traverseRec(func=lvlprint)
    """
    #nlist, plist = tree.BFS()
    #for node,parent in zip(nlist,plist):
    #    print(node.val, parent.val)
        
    #tree.traverseRec('postorder')
    #tree.traverseIter('postorder')
    
    #tree = coolBSTree1()
    #print(getNodeHeight(tree.root))
    #print(isBalanced1(tree.root))
    #print(isBalanced2(tree.root))
    #print(isBST(tree.root,None,None))
    #tree.traverseRec(func=lvlprint)
    #nlist, plist = tree.BFS()
    #for node,parent in zip(nlist,plist):
    #    print(node.val, parent.val)
    
    
    tree,tn1,tn2 = Btree2Node()
    #ans = CommonAncestor1(tree.root,tn1,tn2)
    #print(ans.val)
    #ans2 = CommonAncestor2(tree.root,tn1,tn2)
    #print(ans2.val)
    tree.BFS()
    

if __name__ == '__main__':
    main()