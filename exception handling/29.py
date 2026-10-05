file = open("numbers.txt", "r")
for line in file:
    print(int(line))
    print("File not found")
    print("Invalid data in file")