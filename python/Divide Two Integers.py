class Solution(object):
    def divide(self, dividend, divisor):
        maxR = 2147483647
        minR = -2147483648
        import sys
        if divisor == 0:
            return maxR
        if dividend == 0:
            return 0
        isF = (dividend > 0 and  divisor < 0) or (dividend < 0 and  divisor > 0)
        dd = abs(dividend)
        divisor = abs(divisor)

        rtype = 0
        if divisor == 1:
            rtype = dd
        elif divisor == 2:
            rtype = dd >> 1
        else:
           divilist = map(lambda ch:int(ch),list(string(dividend)))
           q = 0
           r = 0
           d = 0
           for shu in divilist:
               if d < divisor:
                   d = d*10 + shu
                   q = q*10
                   continue
                tempq = 0
                while d>=divisor:
                    tempq+=1
                    d -= divisor
                tempq   

        if isF:
            rtype = 0 - rtype
        if rtype > maxR:
            rtype = maxR
        if rtype < minR:
            rtype = minR
        return rtype

s = Solution()
print s.divide(10,3)