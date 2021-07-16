
def one():
    print("I am one")
    two()

def two():
    print("I am two")
    one()

print("Welcome")
one()
two()
print("Getout")
