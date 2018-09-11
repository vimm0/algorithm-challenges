# Arithmetic operators in Python

x = 15
y = 4

# Output: x + y = 19
print('x + y =', x + y)

# Output: x - y = 11
print('x - y =', x - y)

# Output: x * y = 60
print('x * y =', x * y)

# Output: x / y = 3.75
print('x / y =', x / y)

# Output: x // y = 3
print('x // y =', x // y)

# Output: x ** y = 50625
print('x ** y =', x ** y)

#  Comparison operators in Python
x = 10
y = 12

# Output: x > y is False
print('x > y  is', x > y)

# Output: x < y is True
print('x < y  is', x < y)

# Output: x == y is False
print('x == y is', x == y)

# Output: x != y is True
print('x != y is', x != y)

# Output: x >= y is False
print('x >= y is', x >= y)

# Output: x <= y is True
print('x <= y is', x <= y)

# Logical operators

x = True
y = False

# Output: x and y is False
print('x and y is', x and y)

# Output: x or y is True
print('x or y is', x or y)

# Output: not x is False
print('not x is', not x)

#  Identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

# Membership operators
x = 'Hello world'
y = {1: 'a', 2: 'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)


def itemgetter(*items):
    if len(items) == 1:
        item = items[0]

        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g


print(itemgetter(1)('ABCDEFG'))
# 'B'
print(itemgetter(1, 3, 5)('ABCDEFG'))
# ('B', 'D', 'F')
print(itemgetter(slice(2, None))('ABCDEFG'))
# 'CDEFG'

#  Inplace Operators
a = 'hello'
print(iadd(a, ' world'))
# 'hello world'
print(a)
# 'hello'
s = ['h', 'e', 'l', 'l', 'o']
print(iadd(s, [' ', 'w', 'o', 'r', 'l', 'd']))
# ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(s)
# ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']