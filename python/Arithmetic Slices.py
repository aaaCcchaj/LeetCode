class Solution(object):
    def numberOfArithmeticSlices(self, A):
        chaList = []
        for index in range(len(A) - 1):
            chaList.append(A[index+1] - A[index])
        
        chachaList = []
        for chaIndex in range(len(chaList) - 1):
            chacha = chaList[chaIndex + 1] - chaList[chaIndex]
            chachaList.append(chacha)
        
        zeroCounts = []
        
        zeroCount = 0
        for chachaIndex in range(len(chachaList)):
            if(chachaList[chachaIndex] == 0 ):
                zeroCount = zeroCount + 1
                if chachaIndex == len(chachaList) - 1:
                    zeroCounts.append(zeroCount)
            elif zeroCount > 0:
                zeroCounts.append(zeroCount)
                zeroCount = 0
        
        allCount = 0
        for cha in zeroCounts:
            maxSliceCount = cha + 2
            allCount = allCount + 1
            for iter in range(3,maxSliceCount):
                allCount = allCount + (maxSliceCount - iter +1 )
        
        return allCount

            

s = Solution()
A = [0,0,0,0,0]
print s.numberOfArithmeticSlices(A)