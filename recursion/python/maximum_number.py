def maxed(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]

    current = maxed(list[1:])
    return list[0] if list[1] > current else current

print(maxed([1,4,7,9,4]))