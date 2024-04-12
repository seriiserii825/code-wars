# Anisogram is a word that has no repe:
# letters, consecutive or non-consecutive. Implement a function that determines whether a string that,
# contains only letters is an isogram. Assume the empty stringis an isogram. Ignore letter case.
# Example: (Input —> Output)
# “Dermatoglyphics” --> true
# “aba” --> false
# “mo0se" --> false (ignore letter case)
def isograms(string):
    # return True if len(set(string)) != len(string) else False
    return True if len(set(string.lower())) == len(string.lower()) else False

print(isograms('myNewstr'))

