class InvalidMarksError(Exception):
    pass
    def _init_(self,marks):
        if marks<0 or marks > 100:
            raise InvalidMarksError("Invalid marks")
        self.marks = marks
    marks=85
    def grade(self):
        if self.marks>=90:
            print("grade A")
        elif self.marks>=75:
            print("grade B")
        else:
            print("grade c")
            marks=85
    print("Valid marks")

