class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self,num):
        if(num == 0):
            return 0
        count = 32
        mo = 0
        while num > 1:
            mo = mo<<1 | num%2
            num =num/2
            count = count-1
        mo = mo<<1 | 1
        count = count-1
        mo = mo<<count
        return mo


s = Solution()
print s.reverseBits(43261596 )