
def duplicateCount(string):
    text = string.lower()
    dictionary = {i: text.count(i) for i in text}
    return len([c for c in dictionary if dictionary[c] > 1])

print(duplicateCount('112233445'))
