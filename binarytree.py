#! /usr/bin

from random import shuffle
from Queue import Queue

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
shuffle(numbers)
print numbers
print ''

class TreeNode:
  def __init__(self, nodeData):
    self.data = nodeData
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def insert(self, nodeData, root):
    if root == None:
      self.root = TreeNode(nodeData)
      print 'Root: ' + str(self.root.data)
    else:
      if nodeData <= root.data:
        if root.left == None:
          root.left = TreeNode(nodeData)
        else: 
          self.insert(nodeData, root.left)
      else:
        if root.right == None:
          root.right = TreeNode(nodeData)
        else:
          self.insert(nodeData, root.right)

  def depthFirst(self, node):
    print str(node.data)
    if node.left != None:
      self.depthFirst(node.left)
    if node.right != None:
      self.depthFirst(node.right)

  def depth(self, node):
    lcount = 0;
    rcount = 0;
    if node == None:
      return 0;
    if node.left != None:
      lcount = self.depth(node.left)
    if node.right != None:
      rcount = self.depth(node.right)
    return 1 + max(rcount, lcount)      

  def breadthFirst(self, node):
    q = Queue()
    q.put(self.root)
    while not q.empty():
      t = q.get()
      print str(t.data)
      if t.left != None:
        q.put(t.left)
      if t.right != None:
        q.put(t.right)

tree = Tree()
for n in numbers:
  tree.insert(n, tree.root)

print 'Depth: ' + str(tree.depth(tree.root))
print 'Depth-first (preorder) traversal: '
tree.depthFirst(tree.root)
print 'Breadth-first traversal: '
tree.breadthFirst(tree.root)
#tree.printTree()
#print tree.depth(tree.root);
