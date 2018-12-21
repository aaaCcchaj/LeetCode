import threading

class Solution(object):
    def __init__(self):
        self.counts = []
    def countBits1(self,x):
        count = 0
        while x != 0:
            count = count+(x & 1)
            x = x>>1
        return count
    def hammingDistance(self, pairs):
        count = 0
        for pair in pairs:
            vaal = pair[0]^pair[1]
            count = count + self.countBits1(vaal)
        self.counts.append(count)
    def totalHammingDistance(self, nums):
        count = 0
        allPair = []
        for fIndex in range(len(nums)):
            for sIndex in range(fIndex+1,len(nums)):
                if nums[fIndex] ==nums[sIndex]:
                    continue
                allPair.append([nums[fIndex],nums[sIndex]])
        threadCount = len(allPair)/1000
        threads = []
        for i in range(threadCount + 1):
            procPair = allPair[i*1000:(i+1)*1000]
            thread = threading.Thread(target = self.hammingDistance,args = (procPair,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

        return sum(self.counts)

        """
        :type nums: List[int]
        :rtype: int
        """

s = Solution()
print s.totalHammingDistance([1, 1, 1,2])