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


def test_booleans():
    """Boolean
    Booleans represent the truth values False and True. The two objects representing the values
    False and True are the only Boolean objects. The Boolean type is a subtype of the integer type,
    and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the
    exception being that when converted to a string, the strings "False" or "True" are returned,
    respectively.
    """

    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # Let's try to cast boolean to string.
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"
