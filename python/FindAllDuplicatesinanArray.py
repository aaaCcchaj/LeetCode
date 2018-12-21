class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedNums = sorted(nums)
        result = []
        numsCount = len(nums)
        for index in range(numsCount):
            if(index >= numsCount - 1):
                break
            if sortedNums[index] == sortedNums[index+1]:
                result.append(sortedNums[index])
                index = index + 2
            else:
                index = index + 1
        return result
