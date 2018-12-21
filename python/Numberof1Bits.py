class Solution(object):
    def hammingWeight(self, num):
        if(num == 0):
            return 0
        mo = 0
        while num > 1:
            mo = mo + num%2
            num =num/2
        mo = mo + 1
        return mo

s = Solution()
print s.hammingWeight(15)