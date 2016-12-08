'''
node_map = {}
def b_search(root, val):
    if root.val == val:
        return map_back(root)
    if root.val < val and root.right:
        add_to_map(root, root.right)
        b_search(root.right)
    elif root.val > val and root.left:
        add_to_map(root, root.right)
        b_search(root.left)
    else:
        return None

def add_to_map(parent, child):
    node_map[child] = parent

def map_back(node):
    while node in node_map and not node_map[node].val < node.val:
        node = node_map[node]
    if node == original_root:
        return None
    return node_map[node]
'''

original_root = None

def main(root, val):
    original_root = root
    return b_search(root, val)

def b_search(root, val):
    if not root:
        return None
    if root.val == val:
        return map_back(root)
    if root.val < val and root.right:
        return b_search(root.right, val)
    elif root.val > val and root.left:
        return b_search(root.left, val)
    else:
        return None

def add_to_map(parent, child):
    node_map[child] = parent

def map_back(node):
    while node.parent and node.parent.val > original_root.val:
        node = node.parent
    if node.parent and node.parent.val < original_root.val:
        return node.parent
    return None
