class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitChar = ' '
        oriStrList = s.split(splitChar)
        oriStrList.reverse()
        reverseStr = ''
        for word in oriStrList:
            if word != '':
                reverseStr = reverseStr+ word +' '
        return reverseStr.strip()

s = Solution()
print s.reverseWords("the sky is blue")