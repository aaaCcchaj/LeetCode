class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        t = T
        result = ''
        for c in S:
            rArr = [c for count in range(0, t.count(c))]
            result = result + ''.join(rArr)
            t = t.replace(c,'')
        return result + t
s = Solution()
print s.customSortString("cba","abcd")