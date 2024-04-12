# Check to see if a string has the same amount of 'x’s and ‘o's. The method must return a boolean and be case insensitive. The string can contain any
# char.
# Examples input/output:
# XO(“ooxx") => true
# XO(“xooxx") => false
# X0(“ooxXm")
# X0(“zpzpzpp") => true // when no ‘x’ and ‘o' is present should return true
# true
# X0(“zzoo") => false
def exesAndOhs(string):
    return string.lower().count('x') == string.lower().count('o')

print(exesAndOhs('ooxx'))
print(exesAndOhs('xooxx'))
print(exesAndOhs('Xoox'))
