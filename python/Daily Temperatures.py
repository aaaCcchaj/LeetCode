class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        daily = []
        chalist = []
        max = 0
        for index in range(1,len(temperatures)):
            chalist.append(temperatures[index] - temperatures[index - 1])
        hiIndexs = [] 
        for index in range(len(chalist)):
            if chalist[index] <= 0:
                hiIndexs.append(index)
        if(hiIndexs[len(hiIndexs) - 1] != len(temperatures) - 1):
            hiIndexs.append(len(temperatures) - 1)
        beginIndex = 0
        for hiIndex in hiIndexs:
            for hiRange in range(beginIndex,hiIndex):
                daily.append(1)
            for oriIndex in range(hiIndex + 1,len(temperatures)):
                if temperatures[hiIndex] == max:
                    daily.append(0)
                    break;
                if(temperatures[oriIndex] > temperatures[hiIndex]):
                    daily.append(oriIndex - hiIndex)
                    break
                if oriIndex == len(temperatures) - 1:
                    daily.append(0)
                    max = temperatures[hiIndex]
                    
            beginIndex = hiIndex + 1
        daily.append(0)    
        return daily
            

temperatures =[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47] #[3,1,1,2,1,1,0,1,1,0]
s = Solution()
print s.dailyTemperatures(temperatures)