class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Algorithm:
    ## first - using recursion step by step
    def invertTree(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        root.left, root.right = self.switch(root.right), self.switch(root.left)
        return root
    
    def switch(self, root):
        if not root:
            return None
        left, right = root.left, root.right
        root.left, root.right = self.switch(right), self.switch(left)
        return root

    ## second - short version 
    def invertTree_1(self, root):
        if root:
            root.left, root.right = self.invertTree_1(root.right), self.invertTree_1(root.left)
        return root
    
    ## thrid iterative way
    def invertTree_2(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
            else:
                continue
        return root
        
### test case ###

'''
     4
   /   \
  2     7   
 / \   / \
1   3 6   9

>>> should invert to:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

t1 = TreeNode(4)
t2 = TreeNode(2)
t3 = TreeNode(7)
t4 = TreeNode(1)
t5 = TreeNode(3)
t6 = TreeNode(6)
t7 = TreeNode(9)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7

algo = Algorithm()
print(algo.invertTree(t1))