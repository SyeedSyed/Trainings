print("Hello")

a = 1000 # Global Variable

def show():
    print("I am show")
    print(a)

def display():
    print("I am display")
    print(a)


print(a)
show()
display()
print("Bye")
