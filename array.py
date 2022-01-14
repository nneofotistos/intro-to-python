numbers = [1, 2, 3, 4]
def double_number(num):
    return num + num

result = map(double_number, numbers)
print('before', result)
print('after making it a list', list(result))

result2 = map(lambda x: x + x, numbers)
print('result two -> list', list(result2))

result3 = map(lambda y: y*y, numbers)
print('result three -> list', list(result3))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result4 = map(lambda x, y: x + y, numbers1, numbers2)