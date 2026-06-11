students = []
while True:

    print('\n==== Student Management System ====')
    print('1. Add New Student')
    print('2. View Students')
    print('3. Search Student')
    print('4. Update marks')
    print('5. Exit')

    choice = int(input('Choose (1/2/3/4): '))

    if choice == 1:
        print('Add New Student Selected')

    elif choice == 2:
        print('View Students Selected')

    elif choice == 3:
        print('Search Student Selected')

    elif choice == 4:
        print('Update marks selected')

    elif choice == 5:
        print('Thank you')    
        break
    else:
        print('Invalid Choice')



    if choice == 1:

        name = input('Enter the name of student: ')
        branch = input('Enter the branch of student: ')
        student_id = input('Enter the student id: ')
        marks = int(input('Enter the student marks: '))
        student = {
            "name": name,
            "branch": branch,
            "student_id": student_id,
            "marks": marks
            }
        students.append(student)
        print("Student Added Successfully")

    elif choice == 2:
        if len(students) == 0:
            print('There is no student')

        else:    
            print('----------------------')
            for student in students:
                print(f'Student Name : {student['name']}')
                print(f'Branch: {student['branch']}')
                print(f'Student_id: {student['student_id']}')
                print(f'Marks: {student['marks']}')
            print('----------------------')        

    elif choice == 3:

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


    elif choice == 4:
        id = input('Enter the student_id: ')
        updated_marks = int(input('Enter the new marks: ')) 
        found = False
        for s in students:
            if s['student_id']== id:
                s['marks']= updated_marks  
                found = True
                print('Marks Updated Successfully') 
                break 
        if found == False:
            print('Student not found')


        
        

        
