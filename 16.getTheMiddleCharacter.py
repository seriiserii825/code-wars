# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If
# the word's length is even, return the middle 2 characters.
# #Examples:
# Kata.getMiddle("test") should return “e:
# kata.getMiddle("testing") should return “t”
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return
# def getTheMiddleCharacter(word):
#     if len(word) % 2 == 0:
#         middle_char = word[int(len(word)/2 - 1):int(len(word)/2 + 1)]
#     else:
#         middle_char = word[int(len(word)/2):int(len(word)/2 + 1)]
#     print(middle_char)
#
# getTheMiddleCharacter('string')


def getTheMiddleCharacter(s):
    if len(s) % 2 == 0:
        print(s[len(s) // 2])
    else:
        print(s[len(s) // 2 -1:len(s) // 2 +1])


getTheMiddleCharacter('strng')
