print('---- map ----')
# map
numbers = [1, 2, 3, 4]
def double_number(num):
    return num + num

result = map(double_number, numbers)
print('before', result)
print('after making it a list', list(result))

def triple_number(num):
    return num * 3

triple_result = map(triple_number, numbers)
print('TRIPLE ->', list(triple_result))

result2 = map(lambda x: x + x, numbers)
print('result two -> list', list(result2))

triple_result2 = map(lambda x: x * 3, numbers)
print('TRIPLE result two -> list', list(triple_result2))

result3 = map(lambda y: y * y, numbers)
print('result three -> list', list(result3))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]
  
result4 = map(lambda x, y: x + y, numbers1, numbers2)
print('result 4 -> list', list(result4))

result5 = map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3)
print('result 5 -> list', list(result5))

# help(filter)
print('---- filter ----')

ages = [23, 17, 21, 20, 19, 34, 40, 41, 22, 25, 27]

young_folks = list(filter(lambda person_age: person_age < 21, ages))
print('Young Folks', young_folks)

grown_folks = list(filter(lambda person_age: person_age >= 21, ages))
print('Grown Folks', grown_folks)

def is_not_21(person_age):
    if person_age < 21:
        return True
    else:
        return False

def is_21(person_age):
    if person_age >= 21:
        return True
    else:
        return False

young_people = list(filter(is_not_21, ages))
print('Young People', young_people)

grown_people = list(filter(is_21, ages))
print('Grown People', grown_people)