#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.lc = None
        self.rc = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def level_traversal(self):
        node_ref = {self.root: (self.root, 0)}
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            lvl = node_ref[node][1]
            print(node.val, lvl)
            if node.lc:
                queue.append(node.lc)
                node_ref[node.lc] = (node, lvl+1)
            if node.rc:
                queue.append(node.rc)
                node_ref[node.rc] = (node, lvl + 1)
        return node_ref

    def __trecs__(self, node, arr, level, method, func):

        if method == 'preorder':
            if node:
                func(node)
                arr.append(node.val)
                self.__trecs__(node.lc, level + 1, method, func)
                self.__trecs__(node.rc, level + 1, method, func)
        elif method == 'inorder':
            if node:
                self.__trecs__(node.lc, level + 1, method, func)
                func(node)
                arr.append(node.val)
                self.__trecs__(node.rc, level + 1, method, func)
        elif method == 'postorder':
            if node:
                self.__trecs__(node.lc, level + 1, method, func)
                self.__trecs__(node.rc, level + 1, method, func)
                func(node)
                arr.append(node.val)
        else:
            print('Wrong method chosen.')

    def traverse_rec(self, method='preorder', func=lambda x: print(x.val)):
        node = self.root
        arr = []
        self.__trecs__(node, arr, 0, method=method, func=func)
        return arr

    def traverse_iter(self, method='preorder', func=lambda x: print(x.val)):
        node_stack = [self.root]
        arr = []
        if method == "preorder":
            while len(node_stack) > 0:
                node = node_stack.pop()
                if node:
                    func(node)
                    arr.append(node.val)
                    node_stack.append(node.rc)
                    node_stack.append(node.lc)

        elif method == "inorder":
            while len(node_stack) > 0:
                node = node_stack.pop()
                if node:
                    node_stack.append(node.rc)
                    node_stack.append(node)
                    node_stack.append(node.lc)
                else:
                    if len(node_stack) > 0:
                        realnode = node_stack.pop()
                        func(realnode)
                        arr.append(realnode.val)

        elif method == "postorder":
            while len(node_stack) > 0:
                node = node_stack.pop()
                if node:
                    node_stack.append(node)
                    node_stack.append(node.rc)
                    node_stack.append(node.lc)
                else:
                    node1 = node_stack.pop()
                    if node1:
                        node_stack.append(None)
                        node_stack.append(node1)
                    else:
                        if len(node_stack) > 0:
                            fnode = node_stack.pop()
                            func(fnode)
                            arr.append(fnode.val)
                            if len(node_stack) > 0:
                                node_stack.append(None)

        else:
            print('Wrong method chosen.')
        return arr

    def __helper_bal__(self, arr, li, ri):
        if li > ri:
            return None
        mid = (li + ri)//2
        node = TreeNode(arr[mid])
        node.lc = self.__helper_bal__(arr, li, mid-1)
        node.rc = self.__helper_bal__(arr, mid+1, ri)
        return node

    def from_array_balanced(self, arr):
        self.root = self.__helper_bal__(arr, 0, len(arr)-1)

    def get_node_height(self, node):
        if node is None:
            return -1
        return max(self.get_node_height(node.lc), self.get_node_height(node.rc)) + 1

    def __helper_isb1__(self, node):
        if node is None:
            return True
        hl = self.get_node_height(node.lc)
        hr = self.get_node_height(node.rc)
        if abs(hl - hr) <= 1:
            return self.__helper_isb1__(node.lc) and self.__helper_isb1__(node.rc)
        else:
            return False

    def is_balanced1(self):
        return self.__helper_isb1__(self.root)

    def __helper_isb2__(self, node):
        if node is None:
            return -1
        hl = self.__helper_isb2__(node.lc)
        hr = self.__helper_isb2__(node.rc)
        if hr is not None and hl is not None:
            if abs(hr-hl) <= 1:
                return max(hr, hl) + 1
            else:
                return None
        else:
            return None

    def is_balanced2(self):
        return self.__helper_isb2__(self.root) is not None


class BST(BinaryTree):

    def addnode(self, val):
        node = TreeNode(val)
        current = self.root
        if current is None:
            self.root = node
            return
        while 1:
            if val > current.val:  # right branch
                if current.rc:
                    current = current.rc
                else:
                    current.rc = node
                    break
            if val < current.val:  # left branch
                if current.lc:
                    current = current.lc
                else:
                    current.lc = node
                    break

    def from_array(self, arr):
        for val in arr:
            self.addnode(val)


def main():
    """
    arr = list(range(1,16))
    tree = Tree()
    tree.root = BSTFromSortedArr(arr,0,len(arr)-1)
    tree.traverseRec(func=lvlprint)
    """
    # nlist, plist = tree.BFS()
    # for node,parent in zip(nlist,plist):
    #    print(node.val, parent.val)

    # tree.traverseRec('postorder')
    # tree.traverseIter('postorder')

    # tree = coolBSTree1()
    # print(getNodeHeight(tree.root))
    # print(isBalanced1(tree.root))
    # print(isBalanced2(tree.root))
    # print(isBST(tree.root,None,None))
    # tree.traverseRec(func=lvlprint)
    # nlist, plist = tree.BFS()
    # for node,parent in zip(nlist,plist):
    #    print(node.val, parent.val)

    tree, tn1, tn2 = Btree2Node()
    # ans = CommonAncestor1(tree.root,tn1,tn2)
    # print(ans.val)
    # ans2 = CommonAncestor2(tree.root,tn1,tn2)
    # print(ans2.val)
    tree.BFS()


if __name__ == '__main__':
    main()
