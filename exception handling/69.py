class InvalidPatientError(Exception):
    pass

class Hospital:
    def add_patient(self, name, age):
        if name == "" or age <= 0:
            raise InvalidPatientError("Invalid patient details")
        print("Patient added")

try:
    h = Hospital()
    h.add_patient("", 20)
except InvalidPatientError as e:
    print(e)