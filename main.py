
from student import Student
from student_manager import StudentManager

manager = StudentManager()

while True:
    print("1. Add Students")

    print("2. View Details")
    print("3. Get marks")
    print("4.exit")

    choice = input("Enter the choice: ")

    if choice == "1":
        try:
           student_id = int(input("Enter the Student_ID: "))
           name = input("Enter the Name: ")
           marks = float(input("Enter the Marks: "))
           s = Student(student_id, name, marks)
           manager.add_students(s)
        except ValueError:
            print("Invalid inputs , Enter the numbers for Student_ID $ Marks")

    elif choice == "2":
        manager.view_student()

    elif choice == "3":
        manager.get_marks()
        
    elif choice == "4":
        print("Exit")
        break

    else:
        print("Invalid choice")
print("___________________________________________________________________")
