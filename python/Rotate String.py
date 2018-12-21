class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        index = A.find(B[0])
        while(index >= 0):
            if A[index:len(A)] + A[0:index] == B:
                return True
            else:
                index = A.find(B[0],index + 1)
        return False

s = Solution()
print s.rotateString('abcde','cdeab')
print s.rotateString('abcde','abced')