class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        allLen = 0
        subStr = []
        
        for curIndex in range(len(s)):
            cha = s[curIndex]
            if cha in subStr:
                lastChaIndex = subStr.index(cha)
                preLen = lastChaIndex + 1
                nextLen = len(subStr) - preLen -1
                if(allLen > max([preLen,nextLen])):
                    subStr = []
                    subStr.append(cha)
                elif preLen > nextLen :
                    allLen = preLen
                    subStr = subStr[lastChaIndex + 1:]
                else:
                    subStr = subStr[lastChaIndex + 1:]
                    allLen = nextLen
            else:
                subStr.append(cha)
                if allLen == 0:
                    allLen = 1
        return allLen

s = Solution()
print s.lengthOfLongestSubstring("pwwkew")