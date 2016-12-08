
class Object:

  
  def __init__(self, val, refs=[]):
    self.val = val
    self.refs = refs

  def copy(self):
    return Object(self.val, refs=self.refs[:])


obj1
obj1.refs[0].val = 1
obj2 = obj1.copy()
obj2.refs[0].val = 2
print(obj1.refs[0].val == obj2.refs[0].val)

def deep_copy(self):
  nodeToCopy = copy_nodes(self)
  connect(nodeToCopy)
  return nodeToCopy[self]

def copy_nodes(obj):
  nodeToCopy = {}
  frontier = [obj] 
  while frontier:
    node = frontier.pop()
    nodeToCopy[node] = Object(node.val)
    for next_node in node.refs:
      if next_node not in nodeToCopy
        frontier.append(next_node)
  return nodeToCopy

def connect(nodeToCopy):
  for node, copy in nodeToCopy.items():
      copy.refs = [nodeToCopy[ref] for ref in node.refs]