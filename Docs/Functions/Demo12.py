
a = 1000
def show():
    #print(a)
    a = 100 
    global a
    a = 99
    print(a)
    
print(a)
show()
print(a)
