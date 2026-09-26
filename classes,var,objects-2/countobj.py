class Student:
    count = 0

student1 = Student()
Student.count += 1
student2 = Student()
Student.count += 1
student3 = Student()
Student.count += 1
print("Total Objects:", Student.count)