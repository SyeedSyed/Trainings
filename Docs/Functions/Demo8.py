# Example on Global and local variables

a = 1000 # Global variable
def show():
    print("I am show")
    print(a)
    b = 20 # Local Variale
    print(b)
    print("Sum = ",a+b)

print("Hi")
print(a)
show()
print(a)
print("Bye")
