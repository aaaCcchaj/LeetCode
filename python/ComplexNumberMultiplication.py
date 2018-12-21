class Solution(object):
    def complexNumberMultiply(self, abStr, cdStr):
        abList = abStr.split('+')
        a = int(abList[0])
        b = int(abList[1][:len(abList[1])-1])

        cdList = cdStr.split('+')
        c = int(cdList[0])
        d = int(cdList[1][:len(cdList[1])-1])

        shi = a*c - b*d
        xu = b*c + a*d
        return str(shi)+'+'+str(xu)+'i'
        """
        :type a: str
        :type b: str
        :rtype: str
        """

tstStr1 = "1+-1i"
tstStr2 = "1+-1i"
s = Solution()
print s.complexNumberMultiply(tstStr1,tstStr2)