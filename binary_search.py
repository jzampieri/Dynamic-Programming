def bb(list, item):
    lower = 0
    higher = len(list) - 1

    while lower <= higher:
        middle = (lower + higher) // 2
        guess = list[middle]
        if guess == item:
            return middle
        elif guess > item:
            higher = middle -1
        else:
            lower = middle + 1
    return None

testing = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

print(bb(testing, 11))
print(bb(testing, 2))