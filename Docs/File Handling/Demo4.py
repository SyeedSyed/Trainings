file_name = input("Enter File Name :")

file = open(file_name,"a")

text = input("Enter Text :")

file.write(text)

file.close()

print("Data Written to File")


