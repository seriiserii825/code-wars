def simplePigLatin(string):
    words = string.split()
    return ' '.join([i[1:] + i[0] + 'ay' if i.isalpha() else i for i in words])

print(simplePigLatin('Pig latin is cool !'))
