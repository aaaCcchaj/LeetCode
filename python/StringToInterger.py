import re


class Solution(object):
    def myAtoi(self, str):
        pattenStr = r"[\+,-]\d*|\d+"
        patten = re.compile(pattenStr)
        allPatter = patten.findall(str)
        if(len(allPatter) == 0 or allPatter[0] == '+' or allPatter[0] == '-'):
            return 0
        result = int(allPatter[0])
        if(2147483647 < result or -2147483648 > result):
            return 0 
        return result


xac = Solution()
print xac.myAtoi(" ++c")
print xac.myAtoi(" +-2")
print xac.myAtoi("2")
print xac.myAtoi("sssdfeew232fdf")
