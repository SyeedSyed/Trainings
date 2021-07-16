# Example on Global variable inside a function

def show():
    global a # Global Variale
    a = 100
    print("I am show")
    print(a)


show()
print(a)
