class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

patient1 = Hospital("Ravi", 30, "Fever", "Dr. Kumar")
patient2 = Hospital("Priya", 25, "Cold", "Dr. Anjali")
patient3 = Hospital("Rahul", 40, "Diabetes", "Dr. Raj")

print(patient1.patient_name, patient1.age, patient1.disease, patient1.doctor_name)
print(patient2.patient_name, patient2.age, patient2.disease, patient2.doctor_name)
print(patient3.patient_name, patient3.age, patient3.disease, patient3.doctor_name)