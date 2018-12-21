class Solution(object):
    def productExceptSelf(self, nums):
        rtype = []
        count0 = nums.count(0)
        if count0 > 1:
            for i in range(len(nums)):
                rtype.append(0)
            return rtype
        all = 1
        if count0 == 1:
            for num in nums:
                if(num != 0):
                    all = all * num
            index0 = nums.index(0)
            for i in range(len(nums)):
                if i == index0:
                    rtype.append(all)
                else:
                    rtype.append(0)
            return rtype
        for num in nums:
                all = all * num
        for i in range(len(nums)):
            rtype.append(all/nums[i])
        return rtype


s = Solution()
for re in s.productExceptSelf([0,0]):
    print re