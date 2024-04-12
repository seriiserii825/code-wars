# Given two integers a and b , which can be positive or negative, find the sum of all the integers between and including them and return it. If the two
# numbers are equal return a or b.
# Note: a and b arenotordered!
# Examples (a, b) -> output (explanation)
# (2, @) --> 1 (4+0=1)
# (a, 2) --> 3 4 +2=3)
# (@, 1) --> 1 (@+1=1)
# (4, 4) --> 4 (a since both are same)
# (-4, 0) --> -1 (1 +0=-1)
# (4, 2) --> 2 (-1+@4+142-2)
def sumOfNumbers(a, b):
    return sum(list(range(a, b+1))) if a < b else sum(list(range(b, a+1)))
