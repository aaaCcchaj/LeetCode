class Solution(object):
    def judgeCircle(self, moves):
        return (moves.count("U")-moves.count("D") ==0) and (moves.count("L")-moves.count("R") ==0)
        