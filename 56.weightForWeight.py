def weightForWeight(string):
    weight = sorted(string.split(), key=summa)
    return ' '.join(weight)

    # weights = []
    # for i in string.split():
    #     weights.append({
    #         "sum": sum([int(k) for k in i]),
    #         "item": i
    #         })
    # sorted_array = sorted(weights, key=lambda x: x['sum'])
    # return ' '.join([i['item'] for i in sorted_array])
def summa(n):
    return sum([int(i) for i in n])

print(weightForWeight("56 64 33 89 21 100 5 99"))
