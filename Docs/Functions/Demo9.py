# If local and global variable names are same ?

a = 1000 # Global variable

def show():
    a = 99 # Local Variable
    print(a)

print(a)
show()
print(a)