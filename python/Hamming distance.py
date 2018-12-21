class Solution(object):
    def countBits1(self,x):
        count = 0
        while x != 0:
            if x & 1 == 1:
                count = count+1
            x = x>>1
        return count
    def hammingDistance(self, x, y):
        all0Count = 31 - self.countBits1(x|y)
        all1Count = self.countBits1(x&y)
        return 31 - all0Count - all1Count
        """
        :type x: int
        :type y: int
        :rtype: int
        """
s = Solution()
print s.hammingDistance(1,1)