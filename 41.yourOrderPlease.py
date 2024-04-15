# def yourOrderPlease(string):
#     words = string.split()
#     words_with_dict = []
#     for word in words:
#         key = [int(i) for i in list(word) if i.isdigit()]
#         words_with_dict.append({'key': key[0], 'word': word})
#     words_with_dict.sort(key=lambda x: x['key'])
#     return ' '.join([str(i['word']) for i in words_with_dict])

# def yourOrderPlease(string):
#     words = string.split()
#     new_str = ''
#     for number in range(1, 10):
#         for word in words:
#             if str(number) in word:
#                 new_str += f' {word}'
#     return new_str

def yourOrderPlease(words):
    return ' '.join([word for i in range(1, 10) for word in words.split() if str(i) in word])


print(yourOrderPlease('firs3 secon5 four1'))
