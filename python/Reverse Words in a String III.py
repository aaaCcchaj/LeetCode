class Solution(object):
    def reverseWords(self, s):
        from collections import deque 
        d = deque()  
        d.extendleft(s)  
        reverseStr = ''.join(d)
        reverseStrArr = reverseStr.split(" ")
        reverseStrArr.reverse()
        result = ''
        for subStr in reverseStrArr:
            result = result + subStr + ' '
        return result.rstrip()

ss = Solution()
sts = "Let's take LeetCode contest"
print(ss.reverseWords(sts))