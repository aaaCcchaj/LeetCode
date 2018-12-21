# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.maxList = []
        pass


    def zunQu(self,node,depth):
        if node == None:
            return
        if len(self.maxList) >= depth + 1 :
            if self.maxList[depth] < node.val:
                self.maxList[depth] = node.val
        else:
            self.maxList.append(node.val)
            
        depth = depth + 1
        self.zunQu(node.left,depth)
        self.zunQu(node.right,depth)
        pass


    def largestValues(self, root):
        self.zunQu(root,0)
        return self.maxList
