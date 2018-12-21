class MyCalendarThree(object):
    def __init__(self):
        self.bookCache = dict()

    def book(self, start, end):
        if start not in self.bookCache:
            self.bookCache[start] = list()
        self.bookCache[start].append(end)

        count = 0

        for key in self.bookCache:
            if start < key and end > key:
                count = count + len(filter(lambda item:item >= start,self.bookCache[key]))
            elif start >= key:
                count = count + len(filter(lambda item:item > start,self.bookCache[key]))

        return count 

        
obj = MyCalendarThree()
print obj.book(10, 20) # returns 1
print obj.book(50, 60) # returns 1
print obj.book(10, 40) # returns 2
print obj.book(5, 15)# returns 3
print obj.book(5, 10) # returns 3
print obj.book(25, 55) # returns 3