class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Iterator():
    def __init__(self, root):
        self.yielded = None
        self.mins = self.in_order(root)
    def in_order(self, node):
        if not node:
            return
        for x in self.in_order(node.left):
            yield x
        yield node.val
        for x in self.in_order(node.right):
            yield x
    def has_next(self):
        if not self.yielded:
            self.yielded = next(self.mins, None)
        return self.yielded != None
    def next(self):
        if self.yielded:
            tmp = self.yielded
            self.yielded = None
            return tmp
        return next(self.mins, None);

root = Node(5)
left = Node(3)
right = Node(7)
root.left = left
root.right = right

iterator = Iterator(root)
print iterator.has_next()
print iterator.next()
print iterator.has_next()
print iterator.next()
print iterator.has_next()
print iterator.next()
print iterator.has_next()
print iterator.next()
