# ALL README Material gets tested here

# 1
idx = "abcde".index("d")
idx = idx + 11
print(idx)
idx * 2
print(idx)

# 2
num = 33
isEven = num % 2 == 0
print(isEven)
print(not isEven)

# 3
str1 = 'marker'
num = len('whiteboard') - len(str1)
print(num)
str2 = 'bootcamp'
print(str2[num].upper())
char = str2[num].lower()
print(char + '!')

# 4
sentence = 'welcome to bootcamp prep'
lastChar = len(sentence) - 1
print(lastChar)
print(sentence[lastChar])

# 5
age = 30
if age > 30:
    print('older than 30')
else:
    print('younger than 30')

# 6
str = 'undertale two babey'
if len(str) > 10:
    print('long string')
else:
    print('short string')

if str[0] == 'p':
    print('starts with p')

# 7
num = 15
if num % 3 == 0:
    print('divisible by 3')
elif num % 5 == 0:
    print('divisible by 5')

# 8 is duplicate

# 9
str1 = 'General Assembly'
if str1[0] == str1[0].capitalize():
    print('starts with a capital')

if str1[len(str1) -1] == str1[len(str1) -1].capitalize():
    print('ends with a capital')

# 10
num1 = -44
if num1 > 0:
    print('positive')
elif num1 < 0:
    print('negative')
else:
    print(0)

if num1 % 2 == 0:
    print('even')
else:
    print('odd')

# 11
num3 = 11
if num3 > 5:
    print('if')

# 12

def fizz_buzz(max):
    for i in range(max):
        if i % 3 == 0 and i % 5 != 0:
            print(i, 'fizz')
        elif i % 5 == 0 and i % 3 != 0:
            print(i, 'buzz')
        elif i % 5 == 0 and i % 3 == 0:
            print(i, 'fizzbuzz')

fizz_buzz(30)