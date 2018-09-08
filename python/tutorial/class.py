# https://docs.python.org/3/tutorial/classes.html
class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        """
        classes like to create objects with instances customized to a specific initial state.
        class may define a special method named __init__()
        """
        self.data = []

    def f(self):
        return 'hello world'


# valid attribute references
print(MyClass.i)  # 12345
print(MyClass.f)  # <function MyClass.f at 0x..>
# More information
print(MyClass.__name__)  # 'MyClass'
print(MyClass.__doc__)  # 'A simple example class'
# Class instantiation uses function notation
x = MyClass()
# invoke special method, because initial data initialized there
x.data  # []
