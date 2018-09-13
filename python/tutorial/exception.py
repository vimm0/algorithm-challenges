# try:
#     ...
# except SomeException:
#     tb = sys.exc_info()[2]
#     raise OtherException(...).with_traceback(tb)

# Exception hierarchy
# BaseException
# +-- SystemExit
# +-- KeyboardInterrupt
# +-- GeneratorExit
# +-- Exception
#      +-- StopIteration
#      +-- StopAsyncIteration
#      +-- ArithmeticError
#      |    +-- FloatingPointError
#      |    +-- OverflowError
#      |    +-- ZeroDivisionError
#      +-- AssertionError
#      +-- AttributeError
#      +-- BufferError
#      +-- EOFError
#      +-- ImportError
#      |    +-- ModuleNotFoundError
#      +-- LookupError
#      |    +-- IndexError
#      |    +-- KeyError
#      +-- MemoryError
#      +-- NameError
#      |    +-- UnboundLocalError
#      +-- OSError
#      |    +-- BlockingIOError
#      |    +-- ChildProcessError
#      |    +-- ConnectionError
#      |    |    +-- BrokenPipeError
#      |    |    +-- ConnectionAbortedError
#      |    |    +-- ConnectionRefusedError
#      |    |    +-- ConnectionResetError
#      |    +-- FileExistsError
#      |    +-- FileNotFoundError
#      |    +-- InterruptedError
#      |    +-- IsADirectoryError
#      |    +-- NotADirectoryError
#      |    +-- PermissionError
#      |    +-- ProcessLookupError
#      |    +-- TimeoutError
#      +-- ReferenceError
#      +-- RuntimeError
#      |    +-- NotImplementedError
#      |    +-- RecursionError
#      +-- SyntaxError
#      |    +-- IndentationError
#      |         +-- TabError
#      +-- SystemError
#      +-- TypeError
#      +-- ValueError
#      |    +-- UnicodeError
#      |         +-- UnicodeDecodeError
#      |         +-- UnicodeEncodeError
#      |         +-- UnicodeTranslateError
#      +-- Warning
#           +-- DeprecationWarning
#           +-- PendingDeprecationWarning
#           +-- RuntimeWarning
#           +-- SyntaxWarning
#           +-- UserWarning
#           +-- FutureWarning
#           +-- ImportWarning
#           +-- UnicodeWarning
#           +-- BytesWarning
#           +-- ResourceWarning