
import pickle

file = open("employee.txt","rb")

idno = pickle.load(file)
name = pickle.load(file)
salary = pickle.load(file)

print(idno,name,salary)

file.close()