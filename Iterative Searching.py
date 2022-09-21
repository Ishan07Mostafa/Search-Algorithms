class Search:
    #an iterative approach is taken
    #to implement the search algorithms

    def __init__(self, file):
        self.file = file
        self.array = self.file.read().split()
        for x in range(len(self.array)):
            self.array[x] = int(self.array[x])
        self.length = len(self.array)

    def printresult(self, number):                 #prints the array and results of each methods
        print(self.array)
        print(f'Value found at index: {number}')

    def linearsearch(self, number):                #the basic searching algorithm among
        for i in range(self.length):               #all searching algorithms
            if self.array[i] == number:            #it is defined as a
                return i                           #sequential searching algorithm
            else:
                continue                           #time complexity: O(n)
        return "Not found"                         #space complexity: O(1)

    def binarysearch(self, number):                #one of the most sought after
        self.array.sort()                          #searching algorithms
        low, high = 0, self.length-1               #splits the array into half
        while low != high:                         #to reduce the searching time
            mid = (low+high)//2                    #to half
            if number == self.array[mid]:          #the array needs to be sorted
                return mid                         #in an ascending order
            elif number > self.array[mid]:
                low = mid + 1                      #time complexity: O(logn)
            elif number < self.array[mid]:         #space complexity: O(1)
                high = mid - 1
        return 'Not found'


#driver code
file = open("Input.txt", "r")                #an input is taken from a text file
s = Search(file)
num = 7

#linear search
l = s.linearsearch(num)
s.printresult(l)            #linear search result

#binary search
b = s.binarysearch(num)
s.printresult(b)            #binary search result