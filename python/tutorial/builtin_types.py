# Integer Types

n = -37
print(bin(n))  # '-0b100101'
print(n.bit_length())  # 6
print((1024).to_bytes(2, byteorder='big'))  # b'\x04\x00'
print(int.from_bytes(b'\x00\x10', byteorder='big'))  # 16
print((-2.0).is_integer())  # True
print(float.fromhex('0x3.a7p10'))  # 3740.0
print(float.hex(3740.0))  # '0x1.d380000000000p+11'

#  Iterator Types
print(container.__iter__())

#  Generator Types

# Sequence Types — list, tuple, range
print([x for x in iterable])
print(list(iterable))
print(tuple(iterable))
print((a,))
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(0, 30, 5)))  # [0, 5, 10, 15, 20, 25]
print(list(range(0, 10, 3)))  # [0, 3, 6, 9]

print(list(range(0, -10, -1)))  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
print(list(range(0)))  # []
print(list(range(1, 0)))  # []
print(range(0, 20, 2))  # range(0, 20, 2)
print(11 in r)  # False
print(10 in r)  # True
print(r.index(10))  # 5
print(r[5])  # 10
print(r[:5])  # range(0, 10, 2)
print(r[-1])  # 18
print(str(b'Zoot!'))  # "b'Zoot!'"
print('01\t012\t0123\t01234'.expandtabs())  # '01      012     0123    01234'


class Default(dict):
    def __missing__(self, key):
        return key


print('{name} was born in {country}'.format_map(Default(name='Guido')))  # 'Guido was born in country'
print('   spacious   '.lstrip())  # 'spacious   '
print('www.example.com'.lstrip('cmowz.'))  # 'example.com'
print('1,2,3'.split(','))  # ['1', '2', '3']
print('1,2,3'.split(',', maxsplit=1))  # ['1', '2,3']
print('1,2,,3,'.split(','))  # ['1', '2', '', '3', '']
