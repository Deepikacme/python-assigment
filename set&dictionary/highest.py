students = {
    "Ravi": 80,
    "Sita": 95,
    "John": 75
}

highest = 0
topper = ""

for name, marks in students.items():
    if marks > highest:
        highest = marks
        topper = name

print(topper)
print(highest)