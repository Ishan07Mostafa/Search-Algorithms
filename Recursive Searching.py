class Search:
    #a recursive approach is taken
    #to implement the search algorithms

    def __init__(self, file):
        self.file = file
        self.array = self.file.read().split()
        for x in range(len(self.array)):
            self.array[x] = int(self.array[x])
        self.length = len(self.array)

    def arraysize(self):                                   #the size of the array is returned
        return self.length-1

    def printresult(self, number):                         #prints the array and results of each methods
        print(self.array)
        print(f'Value found at index: {number}')

    def linearsearch(self, number, index):                 #the basic searching algorithm
        if self.array[index] == number:                    #with a recursive approach
            return index
        else:                                              #time complexity: O(n)
            return self.linearsearch(number, index-1)      #space complexity: O(n)
        return 'Not found'

    def binarysearch(self, number, low, high):             #the similar binary search
        self.array.sort()                                  #algorithm with
        mid = (low + high)//2                              #a recursive approach
        if self.array[mid] == number:
            return mid                                     #time complexity: O(logn)
        elif self.array[mid] > number:                     #space complexity: O(logn)
            return self.binarysearch(number, low, mid)
        elif self.array[mid] < number:
            return self.binarysearch(number, mid, high)
        return 'Not found'



#driver code
file = open("Input.txt", "r")                #an input is taken from a text file
s = Search(file)
x = s.arraysize()
num = 7

#linear search
l = s.linearsearch(num, x)
s.printresult(l)                             #linear search result

#binary search
lower = 0
higher = x + 1
b = s.binarysearch(num, lower, higher)
s.printresult(b)                             #binary search result