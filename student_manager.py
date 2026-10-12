
import json
from student import Student


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_students()

    def add_students(self, s):
        self.students.append(s)
        self.save_students()
        print("Student added successfully")

    def view_student(self):
        if not self.students:
            print("No student found")
            return

        for s in self.students:
            print("--------------------")
            s.details()

    def get_marks(self):
        marks = [s.marks for s in self.students]
        print("All student marks:", marks)

    def save_students(self):
        data = []

        for s in self.students:
            data.append({
                "student_id": s.student_id,
                "name": s.name,
                "marks": s.marks
            })

        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_students(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)

            for item in data:
                s = Student(
                    item["student_id"],
                    item["name"],
                    item["marks"]
                )
                self.students.append(s)

        except FileNotFoundError:
            self.students = []

