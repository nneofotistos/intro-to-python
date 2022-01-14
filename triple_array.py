numbers = [1, 2, 3, 4]
def triple_number(num):
    return num * 3

result = map(triple_number, numbers)
print('before', result)
print('after making it a list', list(result))

result2 = map(lambda x: x + x + x, numbers)
print('result two -> list', list(result2))

result3 = map(lambda y: y * y * y, numbers)
print('result three -> list', list(result3))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]

result4 = map(lambda x, y: x + y, numbers1, numbers2)
print('result 4 -> list', list(result4))

result5 = map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3)
print('result 5 -> list', list(result5))