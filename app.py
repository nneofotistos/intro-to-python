# comment

from xmlrpc.client import ServerProxy


def add(num, num2):
    """
    add 2 numbers
    """

name = "Johnny"

nothing = None

is_working = True
car_off = False

if nothing:
    print('This is true')
    num = 7
    print('car is off')
elif car_off:
    print('this is the second condition')
    print('car_off = true')
elif is_working:
    print('This is working')
else:
    print('This is not true')

if is_working:
    print('This is working also')

# conditional -> this first item that represents
# True, it runs that indented [block]
if is_working:
    print('This is working also')

print(15 / 6)
print (15 // 6)

print("ace of spades".split(" "))

print("ace-of-spades".split("-"))



my_scare = "boo"
my_scare.upper()

print("eggs" in "green eggs and ham")

food = "eggs"
print(food in "green eggs and ham")
print(len(food)) 

a = [1, 23, 12, 99, 82]



state = "Washington State"
year = 1889
n = 42
my_message = f"{state} was the {n}th state to join the us"
print(my_message)

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        print(f'{n} is even...')

n = False
num = 1
while n:
    if num % 2 == 0:
        print(f'{num} is even...')

        if num == 750:
            n = False
            print('End program')
        num += 1

for i in range(1, 751):
    if i % 2 == 0:
        print(f"{i} is even...", '**')

        if i == 750:
            print('End program')

nums = [1,2,3,55,66,44,33,22,11,33,44]
for i in range(len(nums)):
    element = nums[i]
    print(element)

students = [
    {
        "name": "Kimmie",
        "city": "Atlanta"
    },
    {
        "name": "Chris",
        "city": "Salt Lake City"
    },
    {
        "name": "Zack",
        "city": "Los Angeles"
    }
]

for i in range(len(students)):
    student = students[i]
    print(student.get("name"))
    
def say_hello(friend="Tim"):
  print("Hello, {}!".format(friend))

say_hello("Tom")

def move(name, city="Seattle", state="Washington"):
  msg = "{} is moving to {}, {}"
  msg = msg.format(name, city, state)
  print(msg)

move("Charlie", "Los Angeles", "California")
move(city="San Francisco", name="Mark", state="California")

def moving(name, city="Chicago", state="Illinois"):
  msg = "{} is moving to {}, {}"
  msg = msg.format(name, city, state)
  print(msg)

moving("Charlie", "Los Angeles", "California")

def get_cities(students):
    '''Return a [list] of all cities from the students list'''
    # TODO Make a empty list
    # TODO Iterate through the list of student
    # TODO Append each city in the dict to the empty list
    # TODO return the list

    result = []

    for s in students:
        if s.get('city'):
            result.append(s.get('city'))

    return result

print('Cities list: ', get_cities(students))

def get_names(students):

    result = []

    for s in students:
        if s.get('name'):
            result.append(s.get('name'))
        
    return result

print('Names list: ', get_names(students))
