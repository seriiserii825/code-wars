# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still
# correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
# ‘Your taskis to write a function maskify , which changes all but the last four characters into "#' .
# Examples
# "4556364607925616" --> “sivitHHHEHHHESE1E"
# "64607935616" --> " #HAHEESE16"
# 1" --5 ay
# // “What was the name of your first pet?”
# “Skippy” --> “##ippy”
# def creditCardMask(string):
#     first_part = string[:-4]
#     last_part = string[-4:]
#     return ''.join([i.replace(i, '#') for i in list(first_part)]) + last_part 

def creditCardMask(string):
    return (len(string) - 4) * '#' + string[-4:]

print(creditCardMask('3432443223442234'))
print(creditCardMask('soskdjfksdfksjfkdjf'))

