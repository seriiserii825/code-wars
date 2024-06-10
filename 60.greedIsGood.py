def greedIsGood(array):
    total = 0
    if array.count(1) > 3 or array.count(1) < 3:
        total += array.count(1)*100
    else:
        total += 1000

    if array.count(5) > 3 or array.count(5) < 3:
        total += array.count(5)*50
    else:
        total += 500

    for i in [2,3,4,6]:
        if array.count(i) > 3 or array.count(i) < 3:
            total += 0
        else:
            total += i*100
    print(total)

greedIsGood([1,2,3,4,5])



