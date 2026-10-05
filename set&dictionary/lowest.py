students = {
    "Ravi": 80,
    "Sita": 95,
    "John": 60,
    "Anu": 75,
    "Kiran": 85
}

highest = -1
lowest = 101
topper = ""
lowest_scorer = ""

for name, marks in students.items():
    if marks > highest:
        highest = marks
        topper = name

    if marks < lowest:
        lowest = marks
        lowest_scorer = name

print("Topper:", topper, highest)
print("Lowest:", lowest_scorer, lowest)