
# Opening a file in Write mode
file = open("one.txt","w")

# Message to Write into the file
text = '''Hello Python Students
This is Naveen
We are in File Handling Class
Sunday Class @10am'''

# Writing Text to file
file.write(text)

# Save the file and close
file.close()
