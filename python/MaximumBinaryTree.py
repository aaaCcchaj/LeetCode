 #Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        maxValue = max(nums)
        maxIndex = nums.index(maxValue)
        rootNode = TreeNode(maxValue)
        if maxIndex > 0:
            rootNode.left = self.constructMaximumBinaryTree(nums[0:maxIndex])
        if maxIndex != len(nums) - 1:
            rootNode.right = self.constructMaximumBinaryTree(nums[maxIndex+1:len(nums)])
        return rootNode

        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
lst = [3,2,1,6,0,5]
s = Solution()
print s.constructMaximumBinaryTree(lst).val
print s.constructMaximumBinaryTree(lst).left.val
print s.constructMaximumBinaryTree(lst).right.val