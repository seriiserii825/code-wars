def scrambles(s1, s2):
    for i in set(s2):
        if s1.count(i) < s2.count(i):
            return False
    return True

print(scrambles('rkqodlw', 'world'))
print(scrambles('tikok', 'tiktok'))


