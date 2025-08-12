import json

class Patient:
    patient_record ={}
    def __init__(self, patient_id:str, name:str, age:int, gender:str, contract:str, blood_group:str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contract
        self.blood_group = blood_group
        self.current_medication = []

    def register_new_patient(self):
        if self.patient_id not in Patient.patient_record:
            Patient.patient_record.update({
                self.patient_id:{
                    "name":self.name,
                    "age": self.age,
                    "gender":self.gender,
                    "contact": self.contact,
                    "blood_group": self.blood_group,
                    "current_medication": self.current_medication,
                }
            })
            print(f"Patient {self.name} registered successfully.")
        else:
            print(f"Patient with ID {self.patient_id} already exists.")

    def update_patient_detail(self, patient_id, name, age, contract, current_medication):
        if self.patient_id in Patient.patient_record:
            Patient.patient_record[self.patient_id].update({
                "name": name,
                "age": age,
                "contact": contract,
                "current_medication": current_medication
            })
            print(f"Patient with ID {patient_id} details updated successfully.")
        else:
            print(f"Patient with ID {self.patient_id} does not exist.")
    
p1 = Patient("P001", "Alice", 30, "Female", "0123456789", "O+")
p1.register_new_patient()

p1.update_patient_detail("P001", "Alice Smith", 31, "0987654321", "Paracetamol")
print(Patient.patient_record)


class Doctor_management:
    doctor_record = {}
    def __init__(self, doctor_id:str, name:str, specialization:str, contact:str, department:str, consultation_fee:float):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.contact = contact
        self.department = department
        self.consultation_fee = consultation_fee
        self.available_slots = {}
    def add_doctor(self):
        if self.doctor_id not in Doctor_management.doctor_record:
            Doctor_management.doctor_record.update({
                self.doctor_id:{
                    "name":self.name,
                    "specialization": self.specialization,
                    "contact": self.contact,
                    "department": self.department,
                    "consultation_fee": self.consultation_fee,
                    "available_slots": self.available_slots
                }
            })
            print(f"Doctor {self.name} added successfully.")
        else:
            print(f"Doctor with ID {self.doctor_id} already exists.")
    def update_doctor_detail(self, doctor_id, name, specialization, contact, department, consultation_fee):
        if self.doctor_id in Doctor_management.doctor_record:
            Doctor_management.doctor_record[self.doctor_id].update({
                "name": name,
                "specialization": specialization,
                "contact": contact,
                "department": department,
                "consultation_fee": consultation_fee
            })
            print(f"Doctor with ID {doctor_id} details updated successfully.")
        else:
            print(f"Doctor with ID {self.doctor_id} does not exist.")

    def remove_doctor(self, doctor_id):
        if self.doctor_id in Doctor_management.doctor_record:
            del Doctor_management.doctor_record[self.doctor_id]
            print(f"Doctor with ID {doctor_id} removed successfully.")
        else:
            print(f"Doctor with ID {self.doctor_id} does not exist.")
    
    def set_working_hours(self, doctor_id, day, start_time, end_time):
        if self.doctor_id in Doctor_management.doctor_record:
            if day not in Doctor_management.doctor_record[self.doctor_id]["available_slots"]:
                Doctor_management.doctor_record[self.doctor_id]["available_slots"][day] = {
                    "start_time": start_time,
                    "end_time": end_time
                }
                print(f"Working hours for {day} set successfully for doctor {self.name}.")
            else:
                print(f"Working hours for {day} already exist for doctor {self.name}.")

    def remove_working_hours(self, doctor_id, day):
        if doctor_id in Doctor_management.doctor_record:
            if day in Doctor_management.doctor_record[doctor_id]["available_slots"]:
                del Doctor_management.doctor_record[doctor_id]["available_slots"][day]
                print(f"Working hours for {day} removed successfully for doctor {doctor_id}.")
            else:
                print(f"Working hours for {day} do not exist for doctor {doctor_id}.")

    def view_doctor_schedule(self, doctor_id):
        if doctor_id in Doctor_management.doctor_record:
            schedule = Doctor_management.doctor_record[doctor_id]["available_slots"]
            if schedule:
                print(f"Schedule for doctor {doctor_id}: ")
                for day, hours in schedule.items():
                    print(f"{day}: {hours['start_time']} - {hours['end_time']}")
        else:
            print(f"No schedule found for doctor {doctor_id}.")
    
        

d = Doctor_management("D001", "Dr. Smith", "Cardiology", "0123456789", "Cardiology", 500.0)
d.add_doctor()
d.update_doctor_detail("D001", "Dr. John Smith", "Cardiology", "0987654321", "Cardiology", 600.0)
print(Doctor_management.doctor_record)

def save_data():
    with open('data1.json', 'w') as file:
        data ={
            "doctors": Doctor_management.doctor_record,
            "patients": Patient.patient_record
            
        }
        json.dump(data, file)
        print("Data saved successfully.")
        return data
def load_date():
    try:
        with open('data1.json', 'r') as file:
            data = json.load(file)
            print("Data loaded successfully.")
            return data
    except FileNotFoundError:
        print("No saved data found.")
        return {"doctors": {}, "patients": {}}
save_data()
print(load_date())
