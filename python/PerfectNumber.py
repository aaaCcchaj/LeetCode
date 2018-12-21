class Solution(object):
    def checkPerfectNumber(self, num):
        if num < 2:
            return False
        number = 1
        import math
        midDev = int(math.sqrt(num) + 1)
        for devisor in range(2,midDev):
            if num % devisor == 0:
                devisorPair = num / devisor
                if devisor <= devisorPair:
                    number+=devisor
                    number+=devisorPair
                else:
                     break
        return number == num
    pass   