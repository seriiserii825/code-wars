
# The goal of this exercise is to convert a string to a new string where each character in the new stringis "(* if that character appears only oncein the
# original string, or “)” if that character appears more than once in the original string. Ignore capitalization when determining if a character isa
# duplicate.
# Examples
# “dint = (CC
# “recede” "000"
# “Success” “.O)O)"
# TE “yc
# Notes “
# Assertion messages may be unclear about what they display in some languages. If you read “...It Should encode XX" the “XXX” is the expected
# result, not the input!
def duplicateEncoder(string):
    return ''.join(['(' if string.lower().count(i) == 1 else ')' for i in string.lower()])

print(duplicateEncoder('111123456'))
