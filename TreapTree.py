import random
from sys import maxint

class Node:
  def __init__(self,left,right,val,prio):
    self.left = left
    self.right = right
    self.val = val
    self.count = 1
    self.prio = prio

class TreapTree:
  '''
  ### Implementation of Treap Tree
  '''
  def rand(self):
  	return random.randint(1,maxint-1)

  def __init__(self):
    random.seed()   
    self.nil = Node(None,None,0,maxint)
    self.nil.left = self.nil.right = self.nil
    self.root = self.nil

  def insert(self,x):
    self.root = self._insert(x,self.root)

  def remove(self,x):
    self.root = self._remove(x,self.root)

  def display(self):
    self._display(self.root,'')

  def _insert(self,x,node):
    if node is self.nil:
      return Node(self.nil,self.nil,x,self.rand())
    else:
      if x == node.val:
      	node.count += 1
      elif x < node.val:
      	node.left = self._insert(x,node.left)
      	if node.left.prio < node.prio:
      	  node = self.rotateWithLeft(node)
      else:
      	node.right = self._insert(x,node.right)
      	if node.right.prio < node.prio:
          node = self.rotateWithRight(node)
      return node   
		
  def _remove(self,x,node):
    if node is self.nil:
      return node
    else:
      if x < node.val:
        node.left = self._remove(x,node.left)
      elif x > node.val:
        node.right = self._remove(x,node.right)
      else:
        if node.count > 1:
          node.count -= 1
        else:
          if node.left.prio < node.right.prio:
            node = self.rotateWithLeft(node)
          else:
            node = self.rotateWithRight(node)

          if not (node is self.nil):
            node = self._remove(x,node)
          else:
            node.left = self.nil
      return node
 
  def rotateWithLeft(self,node):
  	tmp = node.left
  	node.left = tmp.right
  	tmp.right = node
  	return tmp

  def rotateWithRight(self,node):
  	tmp = node.right
  	node.right = tmp.left
  	tmp.left = node
  	return tmp

  def _display(self,node,s):
    if node is self.nil:
      return 
    self._display(node.left,s+'\t')
    print s,node.val,node.count
    self._display(node.right,s+'\t')


if __name__ == "__main__":
  tree = TreapTree()
  data = [5,7,2,6,7,9,10,1,5,6,7,3,9]

  for x in data:
    tree.insert(x)

  tree.display()
  print '=' * 10
  tree.remove(5)
  tree.display()
  print '=' * 10
  tree.remove(5)
  tree.display()
  print '=' * 10
  tree.remove(3)
  tree.display()
