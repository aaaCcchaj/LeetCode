# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def merageNode(self,t1,t2):
        if t2 is None:
            return
        t1.val = t1.val + t2.val;
        if t1.left is None:
            t1.left = t2.left
        else:
            self.merageNode(t1.left , t2.left)
        if t1.right is None:
            t1.right = t2.right
        else:
            self.merageNode(t1.right , t2.right)

    def mergeTrees(self, t1, t2):
        if t1 is None:
            return t2
        self.merageNode(t1,t2)
        return t1;
        