class Solution(object):
    def selfDividingNumbers(self, left, right):
        numbers = []
        for number in range(left,right+1):
            if number < 10:
                numbers.append(number)
                continue
            numberStr = str(number)
            if(numberStr.find('0') > -1):
                continue
            canSelfDevice = True
            for subNum in numberStr:
                if number % int(subNum) != 0:
                    canSelfDevice = False
                    break;
            if canSelfDevice:
                numbers.append(number)
        return numbers   

        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
