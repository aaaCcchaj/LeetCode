class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        import math
        rect1 = abs(A-C) * abs(B-D)
        rect2 = abs(E-G) * abs(F-H)
        rectConver = abs(A-G) * abs(F-D)
        total = rect1+rect2-rectConver
        if total > 2147483647:
            return 2147483647
        return total
    pass
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """