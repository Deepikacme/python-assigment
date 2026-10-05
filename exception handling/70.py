class InvalidEnrollmentError(Exception):
    pass

class Course:
    def enroll(self,age):
        if age < 18:
            raise InvalidEnrollmentError("Not eligible for envirolment")
        print("Enrollment successful")

try:
    c=Course()
    c.enroll(15)
except InvalidEnrollmentError as e:
    print(e)