class Solution(object):
    def numJewelsInStones(self, J, S):
        count = 0
        for ch in J:
            count+=S.count(ch)
        return count;
        