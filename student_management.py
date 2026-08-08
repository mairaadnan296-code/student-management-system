import json
FILE_NAME = "students.json"

# ================= LOAD STUDENTS =================

def load_students():
    """
    Load student records from the JSON file.
    If the file does not exist, return an empty list.
    """

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# ================= SAVE STUDENTS =================

def save_students(students):
    """
    Save student records into the JSON file.
    """

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ================= GRADE CALCULATION =================

def calculate_grade(marks):
    """
    Calculate grade according to marks.
    """
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# ================= INPUT VALIDATION =================

def get_valid_number(message):
    """
    Accept only whole numbers.
    """
    while True:
        value = input(message)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input! Please enter numbers only.")
def get_valid_name(message):
    """
    Accept only alphabetic characters and spaces.
    """
    while True:
        name = input(message).strip()
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid name! Please enter characters only.")
def get_valid_marks():
    """
    Accept marks between 0 and 100.
    """
    while True:
        marks = input("Enter Marks (0-100): ")
        try:
            marks = float(marks)
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter numeric marks.")
def get_valid_attendance():
    """
    Accept attendance %age  0 to 100.
    """
    while True:
        attendance = input("Enter Attendance Percentage (0-100): ")
        try:
            attendance = float(attendance)
            if 0 <= attendance <= 100:
                return attendance
            else:
                print("Attendance must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def get_valid_phone():
    """
    Accept exactly 11 digits for phone number.
    """
    while True:
        phone = input("Enter Phone Number (exactly 11 digits): ")

        if phone.isdigit() and len(phone) == 11:
            return phone

        else:
            print("Invalid phone number! Please enter exactly 11 digits.")


# ================= ADD COURSE =================

def add_course():
    """
    Take course info from the user.
    """
    course_name = input("Enter Course Name: ")
    marks = get_valid_marks()
    grade = calculate_grade(marks)
    course = {
        "course_name": course_name,
        "marks": marks,
        "grade": grade
    }
    return course

# ================= ADD STUDENT =================

def add_student(students):

    print("\n========== ADD STUDENT ==========")

    student_id = max( [student["student_id"] for student in students], default=0) + 1
    roll_number = get_valid_number("Enter Roll Number: ")
    for student in students:
        if student["roll_number"] == roll_number:
            print("This Roll Number already exists!")
            return
    name = get_valid_name("Enter Student Name: ")
    email = input("Enter Email: ")
    phone = get_valid_phone()
    department = input("Enter Department: ")
    program = input("Enter Degree Program: ")
    attendance = get_valid_attendance()
    courses = []
    print("\n========== ADD COURSES ==========")
    while True:
        course = add_course()
        courses.append(course)
        print("Course added successfully!")
        add_more = input("Do you want to add another course? (yes/no): ").lower()
        if add_more != "yes":
            break

    student = {
        "student_id": student_id,
        "roll_number": roll_number,
        "name": name,
        "email": email,
        "phone": phone,
        "department": department,
        "program": program,
        "attendance": attendance,
        "courses": courses
    }
    students.append(student)
    save_students(students)
    print("\nStudent added successfully!")
    print("Total Courses:", len(courses))

# ================= VIEW STUDENTS =================

def view_students(students):
    print("\n========== ALL STUDENTS ==========")
    if not students:
        print("No students found.")
        return
    for student in students:
        print("-" * 60)
        print("Student ID:", student["student_id"])
        print("Roll Number:", student["roll_number"])
        print("Name:", student["name"])
        print("Email:", student["email"])
        print("Phone:", student["phone"])
        print("Department:", student["department"])
        print("Degree Program:", student["program"])
        print("Attendance:", student["attendance"], "%")
        print("\nCourses:")
        for index, course in enumerate(student["courses"],start=1 ):
            print(f"{index}. {course['course_name']} | "
                f"Marks: {course['marks']} | "
                f"Grade: {course['grade']}")

# ================= PRINT ONE STUDENT =================

def print_student(student):
    print("\n" + "-" * 60)
    print("Student ID:", student["student_id"])
    print("Roll Number:", student["roll_number"])
    print("Name:", student["name"])
    print("Email:", student["email"])
    print("Phone:", student["phone"])
    print("Department:", student["department"])
    print("Degree Program:", student["program"])
    print("Attendance:", student["attendance"], "%")
    print("\nCourses:")
    for index, course in enumerate(
        student["courses"],
        start=1
    ):
        print(
            f"{index}. {course['course_name']} | "
            f"Marks: {course['marks']} | "
            f"Grade: {course['grade']}"
        )
    print("-" * 60)

# ================= SEARCH STUDENT =================

def search_student(students):
    print("\n========== SEARCH STUDENT ==========")
    if not students:
        print("No students found.")
        return
    print("1. Search by Roll Number")
    print("2. Search by Name")
    choice = input("Enter your choice: ")
    if choice == "1":
        roll_number = get_valid_number("Enter Roll Number: ")
        found = False
        for student in students:
            if student["roll_number"] == roll_number:
                print_student(student)
                found = True
        if not found:
            print("Student not found.")
    elif choice == "2":
        name = input("Enter Student Name: ").lower()
        found = False
        for student in students:
            if name in student["name"].lower():
                print_student(student)
                found = True
        if not found:
            print("Student not found.")
    else:
        print("Invalid choice.")

# ================= UPDATE STUDENT =================

def update_student(students):
    print("\n========== UPDATE STUDENT ==========")
    roll_number = get_valid_number(
        "Enter Roll Number: "
    )
    for student in students:
        if student["roll_number"] == roll_number:
            print("\nStudent Found!")
            print("1. Update Name")
            print("2. Update Email")
            print("3. Update Phone")
            print("4. Update Department")
            print("5. Update Degree Program")
            print("6. Update Attendance")
            print("7. Add New Course")
            print("8. Update Course")
            print("9. Delete Course")
            choice = input("Enter your choice: ")
            if choice == "1":
                student["name"] = get_valid_name("Enter New Name: ")
            elif choice == "2":
                student["email"] = input( "Enter New Email: ")
            elif choice == "3":
                student["phone"] = get_valid_phone()
            elif choice == "4":
                student["department"] = input( "Enter New Department: ")
            elif choice == "5":
                student["program"] = input( "Enter New Degree Program: ")
            elif choice == "6":
                student["attendance"] = (get_valid_attendance())
            elif choice == "7":
                new_course = add_course()
                student["courses"].append( new_course)
                print("New course added successfully!")
            elif choice == "8":
                update_course(student)
            elif choice == "9":
                delete_course(student)
            else:
                print("Invalid choice.")
                return
            save_students(students)
            print("Student updated successfully!")
            return
    print("Student not found.")

# ================= UPDATE COURSE =================

def update_course(student):
    courses = student["courses"]
    if not courses:
        print("No courses available.")
        return

    print("\n========== COURSES ==========")

    for index, course in enumerate(
        courses,
        start=1
    ):
        print( f"{index}. {course['course_name']} "
            f"(Marks: {course['marks']}, "
            f"Grade: {course['grade']})"
        )
    course_number = get_valid_number(
        "Enter Course Number to Update: "
    )
    if 1 <= course_number <= len(courses):
        selected_course = courses[ course_number - 1]
        print("1. Update Course Name")
        print("2. Update Marks")
        choice = input(
            "Enter your choice: "
        )
        if choice == "1":
            selected_course["course_name"] = input(
                "Enter New Course Name: "
            )
        elif choice == "2":
            selected_course["marks"] = (
                get_valid_marks()
            )
            selected_course["grade"] = (
                calculate_grade(selected_course["marks"] )
            )
            print("Grade automatically updated.")
        else:
            print("Invalid choice.")
    else:
        print("Invalid course number.")

# ================= DELETE COURSE =================

def delete_course(student):
    courses = student["courses"]
    if not courses:
        print("No courses available.")
        return
    print("\n========== COURSES ==========")
    for index, course in enumerate(
        courses,
        start=1
    ):
        print(f"{index}. {course['course_name']}")

    course_number = get_valid_number("Enter Course Number to Delete: ")
    if 1 <= course_number <= len(courses):
        confirmation = input("Are you sure you want to delete this course? (yes/no): ").lower()

        if confirmation == "yes":
            courses.pop(course_number - 1)
            print("Course deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Invalid course number.")
# ================= DELETE STUDENT =================

def delete_student(students):

    print("\n========== DELETE STUDENT ==========")

    roll_number = get_valid_number("Enter Roll Number: ")
    for student in students:
        if student["roll_number"] == roll_number:
            confirmation = input("Are you sure you want to delete this student? (yes/no): ").lower()
            if confirmation == "yes":
                students.remove(student)
                save_students(students)
                print("Student deleted successfully.")
            else:
                print("Deletion cancelled.")
            return
    print("Student not found.")
# ================= STUDENT STATISTICS =================
def student_statistics(students):
    print("\n========== STUDENT STATISTICS ==========")
    if not students:
        print("No students available.")
        return
    total_students = len(students)
    total_courses = sum(
        len(student["courses"])
        for student in students
    )
    all_marks = [
        course["marks"]
        for student in students
        for course in student["courses"]
    ]
    if all_marks:
        average_marks = (sum(all_marks)/ len(all_marks))
        highest_marks = max(all_marks)
        passed_courses = sum(
            1
            for marks in all_marks
            if marks >= 50
        )

        failed_courses = (len(all_marks)- passed_courses )
    else:
        average_marks = 0
        highest_marks = 0
        passed_courses = 0
        failed_courses = 0
    average_attendance = (  sum(student["attendance"]
            for student in students )/ total_students  )
    print( "Total Students:", total_students )
    print("Total Courses:",total_courses)
    print("Average Marks:",round(average_marks,2)
    )
    print("Highest Marks:",highest_marks)
    print("Passed Courses:", passed_courses)
    print("Failed Courses:",failed_courses)
    print("Average Attendance:", round(average_attendance,2),"%")

# ================= MAIN MENU =================

def display_menu():
    print("\n" + "=" * 50)
    print(  "STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Exit")
    print("=" * 50)

# ================= PROGRAM START =================

students = load_students()
while True:
    display_menu()
    choice = input( "Enter your choice (1-7): ")
    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        search_student(students)
    elif choice == "4":
        update_student(students)
    elif choice == "5":
        delete_student(students)
    elif choice == "6":
        student_statistics(students)
    elif choice == "7":
        print( "\nThank you for using "
            "Student Management System!")
        break
    else:
        print( "\nInvalid choice! "
            "Please select between 1 and 7." )