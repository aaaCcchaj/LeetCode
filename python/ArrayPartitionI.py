'''
Given an array of 2n integers, your task is to group these integers into n pairs of 
integer, say (a1, b1), (a2, b2), ..., (an, bn) 
which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
'''
class Solution(object):
    def arrayPairSum(self, nums):
        sortedNums = sorted(nums)
        rtype = 0
        for i in range(int(len(nums)/2)):
            rtype+=sortedNums[i*2]
        return rtype

ss = Solution
testArr = [1,2,3,2]
ss.arrayPairSum(testArr)