def oddRange(end):
    arr = []

    for i in range(1, end, 2):
        arr.append(i)
    return arr

print(oddRange(13))
print(oddRange(6))