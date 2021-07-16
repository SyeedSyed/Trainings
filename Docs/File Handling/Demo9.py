
file = open("four.txt","r")

list_lines = file.readlines()
print(list_lines)

file.close()

print(list_lines[2])
print(list_lines[-1])
