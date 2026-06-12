import json
import csv
students = []

def add_student():

    student_id = input('Enter the student id: ')
    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists!")
            return
        
    name = input("Enter student name: ")
    if not name.isalpha():
        print("Name should contain only letters")
        return
    
    branch = input('Enter the branch of student: ')
    marks = int(input('Enter the student marks: '))
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100")
        return
    
    student = {
        "name": name,
        "branch": branch,
        "student_id": student_id,
        "marks": marks
        }
    students.append(student)
    save_student()
    print("Student Added Successfully")

def view_student():
    if len(students) == 0:
            print('There is no student')

    else:
        for student in students:    
            print('----------------------')
            print(f"Student Name : {student['name']}")
            print(f"Branch: {student['branch']}")
            print(f"Student_id: {student['student_id']}")
            print(f"Marks: {student['marks']}")
        print('----------------------')     

def search_student():
    search = input('Enter the student_id: ')

    found = False

    for s in students:
        if s["student_id"] == search:
            print("Student Found\n")
            print(f"Student Name : {s['name']}")
            print(f"Branch : {s['branch']}")
            print(f"Student ID : {s['student_id']}")
            print(f"Marks : {s['marks']}")
            found = True
            break
    if not found:
        print("Student Not Found")

def update_marks():
    student_id = input('Enter the student_id: ')
    updated_marks = int(input('Enter the new marks: ')) 
    found = False
    for s in students:
        if s['student_id']== student_id:
            s['marks']= updated_marks  
            found = True
            print('Marks Updated Successfully') 
            break
    save_student()     
    if found == False:
        print('Student not found')     

def delete_student():
    student_id = input('Enter the Student_id: ')
    found = False
    for s in students:
        if s['student_id']==student_id:
            students.remove(s)
            found = True
            print('Student Deleted Successfully!')
            break
    save_student()    
    if found == False:
        print('Student not Found')    

def save_student():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def load_student():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []

def statistics():
    if not students:
        print("No students found!")
        return
    
    print(f'Total Students: {len(students)}')
    marks = []
    for student in students:
        marks.append(student['marks'])
    print(f'Maximum Marks: {max(marks)}')  
    print(f'Minimum Marks: {min(marks)}')  
    print(f'Average Marks: {sum(marks)/len(marks):.2f}')


def export_csv():
    if not students:
        print('No students found!')
        return

    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Branch', 'Student_ID', 'Marks'])

        for student in students:
            writer.writerow([
                student['name'],
                student['branch'],
                student['student_id'],
                student['marks']
            ])

    print('Data exported successfully to students.csv')


load_student()
while True:

    print('\n==== Student Management System ====')
    print('1. Add New Student')
    print('2. View Students')
    print('3. Search Student')
    print('4. Update marks')
    print('5. Delete Student')
    print('6. Statistics')
    print('7. Export CSV')
    print('8. Exit')

    choice = int(input('Choose (1/2/3/4/5/6/7/8): '))

    if choice == 1:
        print('Add New Student Selected')
        add_student()

    elif choice == 2:
        print('View Students Selected')
        view_student()

    elif choice == 3:
        print('Search Student Selected')
        search_student()

    elif choice == 4:
        print('Update marks selected')
        update_marks()

    elif choice == 5:
        print('Delete the student')
        delete_student()

    elif choice == 6:
        print('Statistics selected')
        statistics()

    elif choice == 7:
        print('Export CSV selected')
        export_csv()

    elif choice == 8:
        print('Thank you')    
        break
    else:
        print('Invalid Choice')



             


        
        

        
