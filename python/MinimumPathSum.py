class Solution(object):
    def __init__(self):
        self.cacheDict = dict()


    def dynicSum(self,grid,m,n):
        if m == 0 and n == 0:
            return grid[0][0]
        keyStr = str(m)+":"+str(n)
        if self.cacheDict.get(keyStr) != None:
            return self.cacheDict[keyStr]
        mIndex = 0 
        nIndex = 0
        if m > 0:
            mIndex = m - 1
        if n > 0:
            nIndex = n -1
        result = 0
        if (m == 0 and nIndex == 0) or (mIndex == 0 and n == 0):
            result = grid[m][n] + grid[0][0]
        elif m == 0:
            result = grid[m][n] + self.dynicSum(grid,m,nIndex)
        elif n == 0:
            result = grid[m][n] + self.dynicSum(grid,mIndex,n)
        else:
            result = grid[m][n] + min([self.dynicSum(grid,m,nIndex),self.dynicSum(grid,mIndex,n)])
        self.cacheDict[keyStr] = result
        return result;
        

    def minPathSum(self, grid):
        rows = len(grid)-1
        columns = len(grid[0]) - 1
        return self.dynicSum(grid,rows,columns)

grid = [[11,3,1],[1,5,1],[4,2,3]]
s = Solution()
print s.minPathSum(grid)