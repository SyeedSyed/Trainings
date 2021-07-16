# Writing Employee idno, name and salary into a file

idno = 101 # int type
name = 'Ravi' # str type
salary = 185000.00 # float type

file = open("employee.txt","w")
file.write(idno)
file.write(name)
file.write(salary)
file.close()
print("Data is written to File")

# NOTE : Using write function we can write only string's
