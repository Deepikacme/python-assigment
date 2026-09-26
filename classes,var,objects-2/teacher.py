class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

teacher1 = Teacher("Anjali", "Python", 5)
teacher2 = Teacher("Ravi", "Java", 7)
teacher3 = Teacher("Priya", "SQL", 4)

print(teacher1.name, teacher1.subject, teacher1.experience)
print(teacher2.name, teacher2.subject, teacher2.experience)
print(teacher3.name, teacher3.subject, teacher3.experience)