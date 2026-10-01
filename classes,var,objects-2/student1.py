class Student:
    college_name="ABC College"

    def __init__(self,name):
        self.name=name
student1=Student("Deepika")
student2=Student("Priya")
print(student1.name,student1.college_name)
print(student2.name,student2.college_name)