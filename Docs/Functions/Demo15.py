print("Hi")
def one():
    two()
    print("one")
def two():
    print("two")
def three():
    print("three")
    two()
one()
three()
two()
print("Bye")