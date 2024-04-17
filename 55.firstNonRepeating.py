def firstNonRepeating(string):
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
        else:
            continue
    return False

print(firstNonRepeating('torrent'))
