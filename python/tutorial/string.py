# string operations

"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"  # Implicitly references the first positional argument
"From {} to {}"  # Same as "From {0} to {1}"
"My quest is {name}"  # References keyword argument 'name'
"Weight in tons {0.weight}"  # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"  # First element of keyword argument 'players'.

"Harold's a clever {0!s}"  # Calls str() on the argument first
"Bring out the holy {name!r}"  # Calls repr() on the argument first

'{0}, {1}, {2}'.format('a', 'b', 'c')
# 'a, b, c'
'{}, {}, {}'.format('a', 'b', 'c')  # 2.7+ only
# 'a, b, c'
'{2}, {1}, {0}'.format('a', 'b', 'c')
# 'c, b, a'
'{2}, {1}, {0}'.format(*'abc')  # unpacking argument sequence
# 'c, b, a'
'{0}{1}{0}'.format('abra', 'cad')  # arguments' indices can be repeated
# 'abracadabra'

'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
# 'Coordinates: 37.24N, -115.81W'
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord)
# 'Coordinates: 37.24N, -115.81W'

c = 3 - 5j


# ('The complex number {0} is formed from the real part {0.real} ''and the imaginary part {0.imag}.').format(c)
# 'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)


str(Point(4, 2))
# 'Point(4, 2)'

coord = (3, 5)
'X: {0[0]};  Y: {0[1]}'.format(coord)
# 'X: 3;  Y: 5'

'{:<30}'.format('left aligned')
# 'left aligned                  '
'{:>30}'.format('right aligned')
# '                 right aligned'
'{:^30}'.format('centered')
# '           centered           '
'{:*^30}'.format('centered')  # use '*' as a fill char
# '***********centered***********'
