def dfs(node):
    if node.left:
        yield from dfs(node.left)
    yield node
    if node.right:
        yield from dfs(node.right)

class Node:

    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


tree = Node(3, left=Node(1), right=Node(5))
for node in dfs(tree):
    print(node.value)
