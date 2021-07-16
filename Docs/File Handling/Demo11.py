# Writing Employee idno, name and salary into a file

import pickle

idno = 1212# int type
name = 'Ravi Kumar' # str type
salary = 185000.25 # float type

file = open("employee.txt","wb")

pickle.dump(idno,file)
pickle.dump(name,file)
pickle.dump(salary,file)

file.close()

print("Data Written to File")