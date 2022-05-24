file = open("file.txt", "r")
count = 0
for line in file:
    word = line.split(" ")
    count += len(word)
file.close()

print("The number of words in the file is:", count)
