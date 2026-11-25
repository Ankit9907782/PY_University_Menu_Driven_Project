# University Management System

A console-based University Management System developed using Python and Object-Oriented Programming (OOP). The application helps manage students, professors, courses, enrollments, grades, and academic performance through a menu-driven interface.

## Features

### 1. Student Management
- Register new students.
- View individual student details.
- View all registered students.
- Filter students by semester.
- View enrolled courses.
- Calculate and view student GPA.

### 2. Professor Management
- Register new professors.
- View professor details.
- View all registered professors.
- Assign courses to professors.
- View assigned courses.
- View students enrolled in assigned courses.

### 3. Course Management
- Create new courses.
- View course details.
- View all available courses.
- Manage course capacity.
- View students enrolled in a particular course.

### 4. Course Enrollment
- Allow students to enroll in available courses.
- Prevent duplicate course enrollment.
- Check course availability and capacity.
- Maintain student-course enrollment relationships.

### 5. Grade Management
- Allow professors to assign grades to students.
- Maintain grades for individual course enrollments.
- Calculate GPA based on course credits and grade points.

### 6. Academic Reports
- View students enrolled in a course.
- View courses assigned to professors.
- Find students by semester.
- Identify top-performing students based on GPA.

## Technologies Used

- **Programming Language:** Python
- **Concepts:** Object-Oriented Programming (OOP)
- **Data Structures:** Lists and Dictionaries
- **Programming Techniques:** Functions, Loops, Conditional Statements, Type Hints, and List Sorting.

## OOP Concepts Implemented

- Classes and Objects
- Constructors (`__init__`)
- Instance Attributes and Methods
- Object Relationships
- Association between classes
- Encapsulation through class-based organization
- Type Hints
- Working with collections of objects

## Project Structure

```text
University-Management-System/
│
├── main.py
└── README.md
```

*Note: The structure above represents the basic project organization. Update the filename if your actual Python file has a different name.*

## How to Run the Project

### Prerequisites
- Python 3.10 or above.

### Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the project directory:

```bash
cd University-Management-System
```

3. Run the application:

```bash
python main.py
```

## Application Interface

The application provides a menu-driven interface with three main user sections:

1. Administrator
2. Professor
3. Student

Each section provides access to the operations available to that user role.

## Data Storage

Currently, application data is maintained in Python lists and objects during runtime. Data is not permanently stored after the application exits.

## Future Improvements

- Implement permanent data storage using JSON or PostgreSQL.
- Add exception handling and stronger input validation.
- Introduce user authentication and role-based access control.
- Add automated testing using pytest.
- Improve the application architecture by separating classes and functions into modules.

## Author

**Ankit Ghosh**

