def grade(marks):
        if marks < 0 or marks > 100:
            raise ValueError("Invalid marks")

        if marks>=90:
            print("Grade A")
        elif marks>=75:
            print("Grade B")
        else:
            print("Grade C")
        print("valid marks")
grade(85)