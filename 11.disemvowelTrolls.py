# Trolls are attacking your comment section!
# Acommon way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return anew string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr Isrs LI
# Note: for this kata y isn't considered a vowel.
def disemvowelTrolls(sentence):
    return "".join([i for i in sentence if i not in "aeiouAEIOU"])

print(disemvowelTrolls("This website is for losers LOL!")) # Ths wbst s fr lsrs LL!
print(disemvowelTrolls("Hello World")) # Hll Wrld
