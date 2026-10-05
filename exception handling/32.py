marks=int(input("Enter marks: "))
if marks < 0 or marks > 100:
        raise ValueError("Invalid marks")
print("Valid marks")
print(marks)