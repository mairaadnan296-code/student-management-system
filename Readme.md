# Student Management System

## Project Overview

The Student Management System is a console-based application developed using Python. It is designed to manage student records efficiently and perform basic academic calculations.

The system allows users to add, view, search, update, and delete student records. It also automatically calculates student grades based on marks and provides useful statistics about student performance.

Student data is stored in a JSON file for permanent storage.

---

## Features

### Student Management

- Add new student records
- View all student records
- Search students by Roll Number and Name
- Update student information
- Delete student records


### Course Management

- Add multiple courses for each student
- Update course details
- Delete courses
- Automatic grade calculation according to marks


### Academic Management

- Calculate grades automatically
- Manage attendance percentage
- Generate student performance statistics

Statistics include:

- Total number of students
- Total number of courses
- Average marks
- Highest marks
- Passed courses
- Failed courses
- Average attendance percentage


---

## Technologies Used

- Python
- JSON File Handling
- Functions
- Data Validation
- Console-Based Application


---

## Grade Calculation System

| Marks | Grade |
|------|------|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | F |


---

## Input Validation

The system includes input validation for accurate data entry.

Validation features:

- Student name accepts only alphabets and spaces
- Roll number accepts numbers only
- Phone number requires exactly 11 digits
- Marks must be between 0 and 100
- Attendance percentage must be between 0 and 100


---

## Data Storage

Student records are stored in a JSON file.

File used:

```
students.json
```

The data remains saved even after closing the program.


---

## Project Structure

```
Student-Management-System

│
├── student_management_system.py
├── students.json
└── README.md
```


---

## How to Run the Project

### Requirements

- Python 3.x installed


### Steps

1. Clone the repository:

```
git clone https://github.com/your-username/student-management-system.git
```

2. Open the project folder:

```
cd student-management-system
```

3. Run the Python file:

```
python student_management_system.py
```


---

## Application Menu

```
==================================================
          STUDENT MANAGEMENT SYSTEM
==================================================

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Student Statistics
7. Exit

==================================================
```


---

## Sample Student Record

```json
{
    "student_id": 1,
    "roll_number": 101,
    "name": "Ali Khan",
    "email": "ali@gmail.com",
    "phone": "03001234567",
    "department": "Computer Science",
    "program": "BS Software Engineering",
    "attendance": 90,
    "courses": [
        {
            "course_name": "Python",
            "marks": 85,
            "grade": "A"
        }
    ]
}
```


---

## Learning Outcomes

By developing this project, I learned:

- Python programming concepts
- Functions and modular programming
- File handling using JSON
- CRUD operations
- Input validation techniques
- Data management concepts
- Console application development


---

---

## Screenshots

### Main Menu
![main menu.png](screenshots/main%20menu.png)

### Add Student
![add student.png](screenshots/add%20student.png)

### View Student Records
![view student (2).png](screenshots/view%20student%20%282%29.png)

### Student Statistics
![student statistics.png](screenshots/student%20statistics.png)

### update students

![update student.png](screenshots/update%20student.png)

### delete student

![delete student.png](screenshots/delete%20student.png)

---

## Future Improvements

Possible future improvements:

- Add graphical user interface (GUI)
- Connect application with a database
- Add login authentication system
- Generate student reports
- Export records into PDF format


---

## Author

**Maira Adnan**

Information Technology Student


---

## Internship Task

This project was developed as part of the NexaSecure Software Development Internship Program.

**Week 1 Task:** Programming Fundamentals & GitHub Setup

**Project Type:** Console-Based Student Management System