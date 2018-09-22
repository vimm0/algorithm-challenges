"""Numbers.
@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_numbers.asp
There are three numeric types in Python:
- int (e.g. 2, 4, 20)
    - bool (e.g. False and True, acting like 0 and 1)
- float (e.g. 5.0, 1.6)
- complex (e.g. 5+6j, 4-3j)
"""


def test_integer_numbers():
    """Integer type
    Int, or integer, is a whole number, positive or negative,
    without decimals, of unlimited length.
    """

    positive_integer = 1
    negative_integer = -3255522
    big_integer = 35656222554887711

    assert isinstance(positive_integer, int)
    assert isinstance(negative_integer, int)
    assert isinstance(big_integer, int)
