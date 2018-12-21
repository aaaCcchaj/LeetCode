class Solution(object):
    def singleNumber(self, nums):
        sortedNums = sorted(nums)
        result = 0
        numsLen = len(nums)
        if(numsLen == 1):
            return nums[0]
        for i in range(0 , int(numsLen/2)):
            if sortedNums[i*2] != sortedNums[i*2+1]:
                result =sortedNums[i*2]
                break;
        return result


s = Solution()
arr = [1,3,1,-1,3]
s.singleNumber(arr)