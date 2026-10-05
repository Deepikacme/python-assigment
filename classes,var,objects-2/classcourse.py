class Course:
    institute_name="ABC Institute"

    def __init__(self,course_name,duration):
        self.course_name=course_name
        self.duration=duration
course1=Course("Python","3 Months")
print(course1.institute_name)
print(course1.course_name)
print(course1.duration)