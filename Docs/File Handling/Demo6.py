
file = open("four.txt","a")

print("Enter Text to File To Close Type Q")

while True:
    text = input()
    if text != "Q":
        file.write(text+"\n")
    else:
        break

file.close()
print("Data Written to File")


