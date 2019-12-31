def is_bst(node, minkey=None, maxkey=None):
    if node is None:
        return True
    if (minkey is not None and node.val <= minkey) or (maxkey is not None and node.val > maxkey):
        return False
    if not is_bst(node.lc, minkey, node.val) or not is_bst(node.rc, node.val, maxkey):
        return False
    return True


def is_node_in_tree(root, node):
    if root is None or node is None:
        return False
    if root.val == node.val:
        return True
    else:
        return is_node_in_tree(root.lc, node) or is_node_in_tree(root.rc, node)


def common_ancestor1(root, n1, n2):

    if n1 == n2:
        return n1
    if n1 is None or n2 is None or root is None:
        return None

    def helper_ca1(root, node, path):
        if root is None:
            return False
        if root.val == node.val:
            path.append(root)
            return True
        ans = helper_ca1(root.lc, node, path) or helper_ca1(root.rc, node, path)
        if ans is True:
            path.append(root)
        return ans

    path1 = [None]
    path2 = [None]
    a1 = None
    if helper_ca1(root, n1, path1) and helper_ca1(root, n2, path2):
        while path1[-1] == path2[-1]:
            a1, a2 = path1.pop(), path2.pop()
        if a1:
            return a1
        else:
            return a2
    else:
        return None


def common_ancestor2(root, n1, n2):

    def helper_ca2(root, n1, n2):
        if root is None:
            return None
        if root.val == n1.val or root.val == n2.val:
            return root
        left = helper_ca2(root.lc, n1, n2)
        right = helper_ca2(root.rc, n1, n2)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None

    if n1 == n2:
        return root
    if n1 is None or n2 is None or root is None:
        return None
    return helper_ca2(root, n1, n2)


def successor1(node):
    """
    Prob #4.6, CTCI
    Get the in-order successor to a given node, assuming parent pointers exist
    """
    def helper_suc(node):
        if node.lc is None:
            return node
        else:
            return helper_suc(node.lc)

    if node.rc:
        return helper_suc(node.rc)
    else:
        parent = node.par
        while node is parent.rc and parent is not None:
            node = parent
            parent = node.par
        return parent


def successor2(root, target):
    """
    Get the in-order successor to a node whose value is given, and the root node of the tree it is in.
    Note that the tree is a BST.
    Return the value stored in the successor.
    """
    curr = root
    prev = None
    while curr.val is not target:
        if target > curr.val:
            curr = curr.rc
        else:
            prev = curr
            curr = curr.lc

    if curr.rc:
        curr = curr.rc
        while curr.lc is not None:
            curr = curr.lc
        return curr.val
    else:
        if prev:
            return prev.val
        else:
            return None



