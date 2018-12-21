class Solution(object):
    def countArrangement(self, N):
        canDevisiable = []
        for devisiable in range(1,N):
            for needdevisiable in range(devisiable + 1 , N+1):
                if(needdevisiable % devisiable == 0 or devisiable % needdevisiable == 0):
                    canDevisiable.append([devisiable,needdevisiable])
        return canDevisiable.count() 
            
        """
        :type N: int
        :rtype: int
        """

s = Solution()
print s.countArrangement(4)