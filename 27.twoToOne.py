# Take 2strings s1 and s2 including only letters from a to z. Return anew sorted string, the longest possible, containing distinct letters - each
# taken only once - coming from s1 or s2.
# Examples:
# a = “xyaabbbccccdefww”
# b = “sooyyyyabk1mopq”
# longest (a, b) -> “abcdefkLmopqwxy”
# a = “abcdefghijklmnopqrstuvwxy2”
# longest(a, a) -> “abcdefghijkimnopqrstuvwxyz"
def twoToOne(a1, a2):
    return ''.join(sorted(set(a1 + a2)))
