# Simple, given astring of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
def shortestWord(sentence):
    return min([len(i) for i in sentence.split()])

print(shortestWord('Simple, given astring of words, return the length of the shortest word'))

