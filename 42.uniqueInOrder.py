def uniqueInOrder(iterable):
    s = []
    for i in range(len(iterable)):
        if i == 0 or iterable[i] != iterable[i - 1]:
            s.append(iterable[i])
            print(f's: {s}')
    return s

print(uniqueInOrder('aaabbbaaacccdd'))
