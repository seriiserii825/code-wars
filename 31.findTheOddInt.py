# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
# h
# Examples
# [7] should return 7 , because it occurs 1 time (which is odd).
# [2] should return @ , because it occurs 4 time (which is odd).
# [1,1,2] should return 2 , because it occurs 4 time (which is odd).
# [@,1,0,1,0] should return @ , because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] shouldreturn 4 , because it appears 4 time (which is odd).
def findTheOddInt(array):
    return min([i for i in array if array.count(i) % 2 != 0])

print(findTheOddInt([1,2,3,4,5,2,1,2,3]))
