class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsCount = len(nums)
        index = 0
        while index < numsCount:
            if index == numsCount - 1:
                return nums[index]
            if nums[index] != nums[index + 1]:
                return nums[index]
            else:
                index = index + 2


s = Solution()
print s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print s.singleNonDuplicate([3,3,7,7,10,11,11])