class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result1 = self.getListSum(l1)
        result2 = self.getListSum(l2)
        result = result1 + result2
        resultNode = ListNode(result % 10)
        curNode = resultNode
        result = result / 10
        while result != 0 :
            nextNode = ListNode( result % 10)
            curNode.next = nextNode
            curNode = nextNode
            result =  result / 10
        return resultNode


    def getListSum(self,l):
        result = 0
        curNode = l
        curIndex = 0
        while curNode != None:
            result = result + curNode.val * (10**curIndex)
            curNode = curNode.next
            curIndex = curIndex + 1
        return result

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()

rr = s.addTwoNumbers(l1,l2)
while rr != None:
    print rr.val
    rr = rr.next