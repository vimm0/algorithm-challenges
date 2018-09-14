# # string operations
#
# "First, thou shalt count to {0}"  # References first positional argument
# "Bring me a {}"  # Implicitly references the first positional argument
# "From {} to {}"  # Same as "From {0} to {1}"
# "My quest is {name}"  # References keyword argument 'name'
# "Weight in tons {0.weight}"  # 'weight' attribute of first positional arg
# "Units destroyed: {players[0]}"  # First element of keyword argument 'players'.
#
# "Harold's a clever {0!s}"  # Calls str() on the argument first
# "Bring out the holy {name!r}"  # Calls repr() on the argument first
#
# '{0}, {1}, {2}'.format('a', 'b', 'c')
# # 'a, b, c'
# '{}, {}, {}'.format('a', 'b', 'c')  # 2.7+ only
# # 'a, b, c'
# '{2}, {1}, {0}'.format('a', 'b', 'c')
# # 'c, b, a'
# '{2}, {1}, {0}'.format(*'abc')  # unpacking argument sequence
# # 'c, b, a'
# '{0}{1}{0}'.format('abra', 'cad')  # arguments' indices can be repeated
# # 'abracadabra'
#
# 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
# # 'Coordinates: 37.24N, -115.81W'
# coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
# 'Coordinates: {latitude}, {longitude}'.format(**coord)
# # 'Coordinates: 37.24N, -115.81W'
#
# c = 3 - 5j
#
#
# # ('The complex number {0} is formed from the real part {0.real} ''and the imaginary part {0.imag}.').format(c)
# # 'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
#
#
# class Point(object):
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def __str__(self):
#         return 'Point({self.x}, {self.y})'.format(self=self)
#
#
# str(Point(4, 2))
# # 'Point(4, 2)'
#
# coord = (3, 5)
# 'X: {0[0]};  Y: {0[1]}'.format(coord)
# # 'X: 3;  Y: 5'
#
# '{:<30}'.format('left aligned')
# # 'left aligned                  '
# '{:>30}'.format('right aligned')
# # '                 right aligned'
# '{:^30}'.format('centered')
# # '           centered           '
# '{:*^30}'.format('centered')  # use '*' as a fill char
# # '***********centered***********'
#
# #  Text Processing Services
# from string import Template
#
# s = Template('$who likes $what')
# s.substitute(who='tim', what='kung pao')  # 'tim likes kung pao'
# d = dict(who='tim')
# Template('Give $who $100').substitute(d)  # Throw error
# Template('$who likes $what').safe_substitute(d)  # 'tim likes $what'

import re

## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig')  # = > found, match.group() == "iii"
match = re.search(r'igs', 'piiig')  # = > not found, match == None

## . = any char but \n
match = re.search(r'..g', 'piiig')  # = > found, match.group() == "iig"

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g')  # = > found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!')  # = > found, match.group() == "abc"

# Repetition Examples
## i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig')  # = > found, match.group() == "piii"

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii')  # = > found, match.group() == "ii"

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')  # = > found, match.group() == "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')  # = > found, match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx')  # = > found, match.group() == "123"

## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar')  # = > not found, match == None
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar')  # = > found, match.group() == "bar"

# Emails Example
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print match.group()  ## 'b@google'
# Square Brackets
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print match.group()  ## 'alice-b@google.com'
# Group Extraction
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print match.group()  ## 'alice-b@google.com' (the whole match)
    print match.group(1)  ## 'alice-b' (the username, group 1)
    print match.group(2)  ## 'google.com' (the host, group 2)

# Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)  ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print email

# findall With Files

# Open file
f = open('test.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'some pattern', f.read())

# findall and Groups
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print tuple[0]  ## username
    print tuple[1]  ## host

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher
