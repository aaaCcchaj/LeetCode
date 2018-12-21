class Solution(object):
    def countBits(self, num):
        result = [0]
        for i in range(1,num+1):
            mo = 0
            v = i
            while v > 1:
                mo = mo + v%2
                v = v/2
            mo = mo + 1
            result.append(mo)
        return result
        """
        :type num: int
        :rtype: List[int]
        """
s = Solution()
print s.countBits(8)