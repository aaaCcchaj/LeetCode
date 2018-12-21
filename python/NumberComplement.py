class Solution(object):
    def findComplement(self, num):
        bitNum = 0
        unZeroNum = num
        while(unZeroNum != 0):
            bitNum = bitNum + 1
            unZeroNum = unZeroNum>>1
        return ~num & (2**bitNum - 1)


s = Solution()
print(s.findComplement(1))
print(s.findComplement(5))