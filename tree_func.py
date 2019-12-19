
from trees import *


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


def common_ancestor1(root, n1, n2):

    if n1 == n2:
        return root
    if n1 is None or n2 is None or root is None:
        return None

    path1 = []
    path2 = []
    a1 = None
    if helper_ca1(root, n1, path1) and helper_ca1(root, n2, path2):
        while path1[-1] == path2[-1]:
            a1, _ = path1.pop(), path2.pop()
        return a1
    else:
        return None


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


def common_ancestor2(root, n1, n2):
    if n1 == n2:
        return root
    if n1 is None or n2 is None or root is None:
        return None
    return helper_ca2(root, n1, n2)

