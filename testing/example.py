def Adder(option1: int, option2: int) -> int:
    """Adds two numbers together."""
    assert type(option1) == int, "option1 is not a integer"
    assert type(option2) == int, "option2 is not a integer"
    return option1 + option2


def myMethod(c: int):
    """Difficult to test method due to complexity and lack of focus"""
    print("hello world")

    x = input("Enter a number")

    y = x * 2

    print(y)

    print(__file__)

    z = dependantMethod() * y * c * dependantMethod2()

def dependantMethod():
    return 4

def dependantMethod2():
    return 8

def Orchestrator():
    """Orchestrator does not need to be tested, so long as we have tested the parts of this"""
    return dependantMethod() * dependantMethod2()