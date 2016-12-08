# Given a binary tree calculate its width where width is the length of the longest path in the tree.

def width(node, heights):
    if not node.left and not node.right:
        return 0
    left_height = heights.get(node.left, -1)
    right_height = heights.get(node.right, -1)
    width_through_root = 2 + left_height + right_height
    left_width = width(node.left)
    right_width = width(node.right)
    return max(width_through_root, left_width, right_width)

def height(node, heights):
    '''
    Fills heights with height of all nodes of subtree of node
    '''
    if node is None:
        return
    if not node.left and not node.right:
        heights[node] = 0
        return
    height(node.left)
    height(node.right)
    heights[node] = 1 + max(heights[node.left], heights[node.right])


heights = {}
height(root, heights)
print width(root, heights)


def height(node, heights):
    '''height returns the height of subtree node and caches it in heights.'''
    if node is None:
        return -1
    if not nodel.left and not node.right:
        heights[node] = 0
        return 0
    heights[node] = 1 + max(height(node.left, heights), height(node.right, heights))
    return heights[nodew]
