from tree import TreeNode


def isSameTree(p, q):
    lsp = []
    lsq = []

    def preorder(node, ls):
        if node:
            ls.append(node.data)
            preorder(node.left, ls)
            preorder(node.right, ls)
        else:
            ls.append('None')

    preorder(p, lsp)
    preorder(q, lsq)
    return lsp == lsq


def isSameTreeFaster(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.data == q.data:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    return False


tree1 = TreeNode(1)
tree1.insert(2)
tree1.insert(2)
tree1.insert(2)

tree2 = TreeNode(1)
tree2.insert(2)
tree2.insert(2)
tree2.insert(2)
tree2.insert(2)

print(isSameTree(tree1, tree2))
print(isSameTreeFaster(tree1, tree2))
