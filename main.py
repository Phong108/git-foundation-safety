title = "Student Manager"
print("student manager")
students = []

def add_student():
    name = input("Nhap ten: ")
    students.append(name)

print("Student Manager")
def search_student():
    print("Search student")
def delete_student():
    pass
def update_student():
    pass
def display_students():
    print("Display student list")
def validate_student_id(student_id):
    return len(student_id) > 0
def count_students(students):
    return len(students)
