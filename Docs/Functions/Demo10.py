# To modify global variable value inside a function
# to do so we use "global" keyword.

a = 1000
def show():
    global a
    a = 99
    print(a)

print(a)
show()
print(a)