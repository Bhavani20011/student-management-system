class Student:
    def __init__(self,student_id,name,marks):
        self.student_id=student_id
        self.name=name
        self.marks=marks
    def details(self):
        print("Student ID:",self.student_id)
        print("Name:",self.name)
        print("Marks:",self.marks)