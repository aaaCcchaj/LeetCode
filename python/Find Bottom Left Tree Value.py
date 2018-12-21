# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.leftVal = 0
        self.leftDepth = 0

    def zunQu(self,node,depth):
        if node == None:
            return
        depth = depth + 1
        if depth > self.leftDepth:
            if node.left != None:
                self.leftVal = node.left.val
                self.leftDepth = depth
            elif node.right != None:
                self.leftVal = node.right.val
                self.leftDepth = depth
        self.zunQu(node.left,depth)
        self.zunQu(node.right,depth)

    def findBottomLeftValue(self, root):
        self.leftVal = root.val
        self.leftDepth = 1
        self.zunQu(root,1)
        return self.leftVal

s = Solution()
type(s)