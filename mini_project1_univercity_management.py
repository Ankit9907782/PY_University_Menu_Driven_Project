# if not function_name():
    # pass
class Student:
    def __init__(self,student_id:int, name:str, semester:int):
        self.student_id = student_id
        self.name = name
        self.semester = semester
        self.enroll = []
        self.total_gpa = None
        print("Student Registered Successfully")
    def enroll_in_course(self,enroll):
        for e in self.enroll:
            if e.course.course_id == enroll.course.course_id:
                return False
        self.enroll.append(enroll)
        return True
    def calculate_gpa(self) -> bool:
        total_credits:float = 0.0
        total_grade_points:int = 0
        if self.total_gpa is not None:
            return True
        if not self.enroll:
            return False
        for enroll in self.enroll:
            if enroll.grade is None:
                return False
            total_credits += enroll.course.credits
            total_grade_points += (enroll.course.credits * enroll.grade_points[enroll.grade])
        self.total_gpa = total_grade_points / total_credits
        return True

class Enrollment:
    def __init__(self, course:Course):
        self.course = course
        self.grade = None
        self.grade_points = {
                "O": 10,
                "A+": 10,
                "A": 9,
                "B+": 8,
                "B": 7,
                "C": 6,
                "D": 5,
                "F": 0
            }
    def show_details(self):
        print(f"{self.course.course_name}    {self.grade}")

class Course:
    def __init__(self, course_id:int, course_name:str, credits:float, capacity:int):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.capacity = capacity
        self.professor = []
        self.student = []
        print("Course Added Successfully")
    def add_professor(self,professor):
        self.professor.append(professor)
    def add_student(self,student):
        self.student.append(student)
        self.capacity = self.capacity - 1

class Professor:
    def __init__(self, professor_id:int, professor_name:str, department:str):
        self.professor_id = professor_id
        self.professor_name = professor_name
        self.department = department
        self.courses = []
        print("Professor Registered Successfully")
    def add_courses(self,course):
        self.courses.append(course)
        course.add_professor(self)                # New important Concept
    def view_courses(self): 
        if not self.courses:
            print("You are not teaching any courses.")
            return 
        print("Your Assigned Courses:\n")
        print("Course Id\t\tCourse Name")
        for course in self.courses:
            print(f"{course.course_id}\t\t{course.course_name}")

    def view_courses_students(self):     # one professor teaches only one course.
        for course in self.courses:
            print(f"{course.course_id}      {course.course_name}")
            if course.student:
                for student in course.student:
                    print(f"{student.student_id}      {student.name}")
                    # return False
            else:
                print("No Student enrolled the courses!")
    def get_students_of_course(self,c_id):
        for course in self.courses:
            if course.course_id == c_id:
                return course.student 
        return None
    
def add_student(Students):             # Done : Register New Student
    student_id:int = int(input("Enter the Student ID: "))
    if find_student_by_id(Students,student_id):              # Important Thing or Concept...
        print("This student already exists!")
        return
    name:str = input("Enter the Student Name:")
    semester:int = int(input("Enter the Student's Semester: "))
    student:Student = Student(student_id,name,semester)
    Students.append(student)

def add_course(Courses):               # Done : Add Course
        course_id:int = int(input("Enter the Course ID: "))
        for cour in Courses:
            if cour.course_id == course_id:
                print("This course already exists!")
                return
        course_name:str = input("Enter the Course Name: ")
        credits:float = float(input("Enter the Credit Points: "))
        capacity:int = int(input("Enter the Capacity: "))
        course:Course = Course(course_id,course_name,credits,capacity)
        Courses.append(course)

def add_professor(Professors):         # Done : Add Professor
    professor_id:int = int(input("Enter the Professor ID: "))
    for prof in Professors:
            if prof.professor_id == professor_id:
                print("This Professor already exists!")
                return
    professor_name:str = input("Enter the Professor Name:")
    department:str = input("Enter the Department: ")
    professor:Professor = Professor(professor_id, professor_name, department)
    Professors.append(professor)  

def assign_grades_by_professor_to_student(Professors):     #I have to add the while for assign the gredes for every students ---- Pending.
    p_id:int = int(input("Enter the Professor ID: "))
    professor:None = None
    for pro in Professors:
        if pro.professor_id == p_id:
            professor = pro
            break
    if professor is None:
        print("Professor Not Found!")
        return
    professor.view_courses_students()
    s_id:int = int(input("Enter the Student ID for assigning the grades: "))
    student:None = None
    for course in professor.courses:
        for stu in course.student:
            if stu.student_id == s_id:
                student = stu
                break
        if student is not None:
            break
    if student is None:
        print(f"This student is not under the guidance of the {professor.professor_name}!")
        return

    for enroll in student.enroll:
        print(f"{enroll.course.course_id}             {enroll.course.course_name}")

    c_id:int = int(input("Enter the Course Id: "))
    enroll_found:None = None
    for enroll in student.enroll:
        if enroll.course.course_id == c_id:
            enroll_found = enroll
            break
    if enroll_found is None:
        print("Course Not Found!")
        return
    found:bool = False
    for cour in professor.courses:
        if cour.course_id == c_id:
            found = True
            break
    
    if not found:
        print("You donot teach this course!")
        return
    grade:str = input(f"Enter the grade for {enroll_found.course.course_id}\t\t{enroll_found.course.course_name}")
    enroll_found.grade = grade
    print("\nGrade Assigned Successfully!\n")
    enroll_found.show_details()

def assign_course_to_professor(Professors,Courses):            # Done : Assign Course (Assigning course to professor.)
    pro_id:int = int(input("Enter The Professor ID: "))
    professor = None
    for pro in Professors:
        if pro.professor_id == pro_id:
            professor = pro
            break

    if professor is None:
        print("Professor Not Found!")
        return
    
    if not Courses:
        print("No Courses have been Created Yet!")
        return
    print("Available Courses: ")
    print("Course ID\t\tCourse Name")
    for course in Courses:
        if course not in professor.courses:
            print(f"{course.course_id}\t\t{course.course_name}")

    print("Your Assigned Courses:\n")
    if not professor.courses:
        print("No Course Assigned Yet!")
    else:
        print("Course ID\t\tCourse Name")
        for assigned_course in professor.courses:
            print(f"{assigned_course.course_id}\t\t{assigned_course.course_name}")
    while True:
        i:int = 0 
        available = len(Courses) - len(professor.courses)

        if available == 0:
            print("All available courses have already been assigned to this professor.")
            return
        n:int = int(input("How many courses you want to add: "))
        if n > available:
            print(f"Only {available} course(s) are available for this professor.")
            print("Your Already Assigned Courses:\n")
            for co in professor.courses:
                print(f"{co.course_id}    {co.course_name}")
            n = available
        while i < n:
            c_id:int = int(input("Enter the Course ID: "))
            course:None = None
            for cour in Courses:
                if c_id == cour.course_id:
                    course = cour
                    break
            if course is None:
                print("Course Not Found")
                continue
            # already_assign_course = course in professor.courses          # New Line concept
            if course in professor.courses:
                print("This Course is already assigned!")
                print("Chose Another Course!")
                continue
            professor.add_courses(course)
            print("The course assigned successfully!")
            i+=1
        break

def view_courses_of_student(Students):                         # Done : View MY Courses.
    if not Students:
        print("Sorry... No Students Are in The University.")
        return
    student_id:int = int(input("Enter the student ID to get the student details: "))
    student: Student | None = find_student_by_id(Students,student_id)
    if student is None:
        print("Student Not Found!")
        return
    if not student.enroll:
        print("No Courses are enrolled...")
        return
    print("Course ID\t\tCourse Name\t\tCredits")
    for enroll in student.enroll:
        print(f"{enroll.course.course_id}\t\t{enroll.course.course_name}\t\t{enroll.course.credits}")

def view_courses_of_professor(Professors):                  # Done : View Courses (Professor can see his assigned courses.)
    pro_id:int = int(input("Enter the Professor's ID: "))
    professor:None = None
    for pro in Professors:
        if pro.professor_id == pro_id:
            professor = pro
            break
    if professor is None:
        print("Professor Not Found.")
        return
    professor.view_courses()

def view_all_courses(Courses):                # Done : View All Courses                       (To show the all Courses. Not Professor)
    if not Courses:
        print("No Course Existed!")
        return
    print("Course Id\t\tCourse Name\t\tCredits")
    for course in Courses:
        print(f"{course.course_id}\t\t{course.course_name}\t\t{course.credits}")

def view_course_details(Courses):
    if not Courses:
        print("Sorry... No Courses Are in The University.")
        return
    course_id: int = int(input("Enter the course ID to get the course details: "))
    course: Course | None = None
    for cour in Courses:
        if cour.course_id == course_id:
            course = cour
            break
    if course is None:
        print("Course not found.")
        return
    print("=" * 50)
    print("Courses Details")
    print("=" * 50)
    print("\n")
    print("ID\t\tName\t\tCapacity\t\tCedits")
    print("\n")
    print(f"{course.course_id}\t\t{course.course_name}\t\t{course.capacity}\t\t{course.credits}")

def view_students_in_a_course(Courses):          # Done : View Students in a Course   (To show the all students who enrolled of the course.)
    c_id:int = int(input("Enter the Course ID To Get All The Students Of This Course: "))
    course:None = None
    for cour in Courses:
        if cour.course_id == c_id:
            course = cour
            break
    if course is None:
        print(f"This Course Of Course ID which is {c_id} Not Found!")
        return
    print(f"Course ID is {course.course_id}, Course Name is {course.course_name}")
    if not course.student:
        print("No students enrolled!")
        return
    print("Enrolled students: ")
    print("\n")
    print("ID\t\tName")
    for student in course.student:
        print(f"{student.student_id}\t\t{student.name}")

def view_students_of_professor(Professors):                 # Done : View Students (To show the students of Professor's Assigned Courses)
    professor_id:int = int(input("Enter the Professor Id: "))
    professor:None = None
    students:None = None
    for pro in Professors:
        if pro.professor_id == professor_id:
            professor = pro
            break
    if professor is None:
        print("Professor Not Found.")
        return
    professor.view_courses()
    while True:
        c_id:int = int(input("Enter the Course id: "))
        students = professor.get_students_of_course(c_id)
        if students is None:
            print("You are not teaching this course!")
            return
        if not students:
            print(f"No student enrolled this course which course ID is {c_id}")
            return 
        print(f"So The Enrolled Students of The Course ID {c_id}:\n")
        print("ID\t\tName")
        for stu in students:
            print(f"{stu.student_id}\t\t{stu.name}")
        conti:int = int(input(f"If You Want To Continue To See The Students Of The Assigned Courses of {professor.professor_name} Press 1 OtherWise Press 0: "))
        if conti == 0:
            break

def view_professor_details(Professors):                     # Done : view professor details
    if not Professors:
        print("Sorry... No Professors Are in The University.")
        return
    prof_id: int = int(input("Enter the professor ID to get the professor details: "))
    professor: Professor | None = None
    for prof in Professors:
        if prof.professor_id == prof_id:
            professor = prof
            break
    if professor is None:
        print("Professor not found.")
        return
    print("=" * 50)
    print("Professors Details")
    print("=" * 50)
    print("\n")
    print("ID\t\tName\t\tDepartment")
    print(f"{professor.professor_id}\t\t{professor.professor_name}\t\t{professor.department}")
    if not professor.courses:
        print("No course assigned yet")
        return
    print("=" * 50)
    print("Assigned Courses")
    print("=" * 50)
    print("\n")
    print("ID\t\tName\t\tCapacity\t\tCedits")
    print("\n")
    for course in professor.courses:
        print(f"{course.course_id}\t\t{course.course_name}\t\t{course.capacity}\t\t{course.credits}")

def view_student_details(Students):              # Done : View Student Details
    if not Students:
        print("Sorry... No Students Are in The University.")
        return
    student_id:int = int(input("Enter the student ID to get the student details: "))
    student: Student | None = find_student_by_id(Students,student_id)
    if student is None:
        print("Student not found!")
        return
    print(f"The Student ID is {student.student_id}\nStudent name is {student.name}\nStudent semester is {student.semester}\n")
    if not student.enroll:
        print("No Courses are enrolled...")
        return
    print("Course ID\t\tCourse Name\t\tGrade")
    for enroll in student.enroll:
        grade:str | None = enroll.grade if enroll.grade is not None else "Not Assigned"
        # grade = enroll.grade or "Not Assigned"                    # Another way to define the grade important to know
        print(f"{enroll.course.course_id}\t\t{enroll.course.course_name}\t\t{grade}")

def students_by_semester(Students):               # Done : Students by Semester
    sem:int = int(input("Enter the semester: "))
    found:bool = False
    if not Students:
        print("No students are registered.")
        return
    print(f"\nStudents of Semester {sem}\n")
    print("Student ID\t\tStudent Name")
    for student in Students:
        if student.semester == sem:
            print(f"{student.student_id}\t\t{student.name}")
            found = True
    if not found:
        print(f"No students found in Semester {sem}.")
        return

def find_student_by_id(Students,student_id) -> Student | None:
    for student in Students:
        if student.student_id == student_id:
            return student
    return None

def print_student_gpa(Students):                # Done : View Transcript
    student_id:int = int(input("Enter the Student Id To print the Student GPA: "))
    student = find_student_by_id(Students,student_id)
    if student is None:
        print("Student Not Found!")
        return
    if student.calculate_gpa():
        print("GPA is calculated Successfully!")
        print(f"Student Name is {student.name}")
        print("Course ID\t\tCourse Name\t\tGrade")
        for enroll in student.enroll:
            print(f"{enroll.course.course_id}\t\t{enroll.course.course_name}\t\t{enroll.grade}\n\n")
        print(f"The total GPA is {student.total_gpa}")
    else:
        print("Unable to calculate GPA.")
        print("Either no courses are enrolled or grades are not assigned!")
    
def top_student_according_to_GPA(Students):          # Done : Top GPA Students
    n:int = int(input("Enter the top position of the student: "))
    if n <= 0:
        print("Please enter a positive number.")
        return
    top_students:list = list()
    for student in Students:
        if student.total_gpa is not None:
            top_students.append(student)
    if not top_students:
        print("No student's GPA has been calculated yet!")
        return
    top:int = min(n, len(top_students))
    top_students.sort(key= lambda student : student.total_gpa, reverse= True)
    print(f"We have top {top} students.\nHere you go...")

    for i in range(top):
        print(f"Top {i+1} student is {top_students[i].name}\t\t{top_students[i].total_gpa: .2f}")   # .2f is called a format specifier in Python where . → decimal point, 2 → show 2 digits after the decimal point, and f → display the number as a floating-point (decimal) number

def calculate_gpa_of_student(Students):              # Done : Calculate GPA
    student_id:int = int(input("Enter the Student ID to get the Result(GPA): "))
    student = find_student_by_id(Students,student_id)
    if student is None:
        print(f"This student who's ID is {id} not found!")
        return
    if student.calculate_gpa():
        print("GPA is calculated Successfully!")
    else:
        print("Unable to calculate GPA.")
    
def student_enroll_in_course(Students,Courses):             # Done : Enroll in Course
    student_id:int = int(input("Enter the Student's ID: "))
    student:Student | None = find_student_by_id(Students,student_id)
    if student is None:
        print("Student Not Found.")
        return
    if not Courses:
        print("No Courses are there...")
        return
    print("Available Courses: ")
    print("ID\t\tName")
    for course in Courses:
        print(f"{course.course_id}\t\t{course.course_name}")
    while True:
        c_id:int = int(input("Enter the Course ID(0 to exit): "))
        if c_id == 0:
            print("Course enrollment completed.")
            break
        course:None = None
        for cou in Courses:
            if cou.course_id == c_id:
                course = cou
                break
        if course is None:
            print("Course Not Found!")
            continue
        if course.capacity <= 0:
            print("This course capacity is full... Sorry!!")
            print("Choice another course...")
            continue
        enroll:Enrollment =Enrollment(course)
        if not student.enroll_in_course(enroll):
            print("Course already enrolled")
            continue
        course.add_student(student)
        print(f"{course.course_name} is enrolled successfully")
        

def view_all_students(Students):              # Done : View All Students
    if not Students:
        print("No students found")
        return
    print("=" * 50)
    print("All Students")
    print("=" * 50)
    print("\n")
    print("ID\t\tName\t\tSemester")
    for student in Students:
        print(f"{student.student_id}\t\t{student.name}\t\t{student.semester}")

def view_all_professors(Professors):           # Done : View All Professors
    if not Professors:
        print("No professors found.")
        return
    print("=" * 50)
    print("All Professors")
    print("=" * 50)
    print("\n")
    print("ID\t\tName\t\tdepartment")
    for professor in Professors:
        print(f"{professor.professor_id}\t\t{professor.professor_name}\t\t{professor.department}")

def student_management(Students):
    while True:
        print("========== STUDENT MANAGEMENT ==========")

        print("1. Add Student")
        print("2. View Student Details")
        print("3. View All Students")
        print("4. Students by Semester")
        print("5. Calculate Student GPA")
        print("6. Print Student GPA")
        print("7. Back")
        choice:int = int(input("Enter the chioce: "))
        if choice == 1:
            add_student(Students)
        elif choice == 2:
            view_student_details(Students)
        elif choice == 3:
            view_all_students(Students)
        elif choice == 4:
            students_by_semester(Students)
        elif choice == 5:
            calculate_gpa_of_student(Students)
        elif choice == 6:
            print_student_gpa(Students)
        elif choice == 7:
            return
        else:
            print("Invalid Chioce...")
           
def professor_management(Professors,Courses):
    while True:
        print("========== PROFESSOR MANAGEMENT ==========")

        print("1. Add Professor")
        print("2. View Professor Details")
        print("3. View All Professors")
        print("4. Assign Course to Professor")
        print("5. View Courses of Professor")
        print("6. Back  ")   
        chioce:int = int(input("Enter the chioce: "))
        if chioce == 1:
            add_professor(Professors)
        elif chioce == 2:
            view_professor_details(Professors)
        elif chioce == 3:
            view_all_professors(Professors)
        elif chioce == 4:
            assign_course_to_professor(Professors,Courses)
        elif chioce == 5:
            view_courses_of_professor(Professors)
        elif chioce == 6:
            return
        else:
            print("Invalid choice")        

def course_management(Courses):
    while True:
        print("========== COURSE MANAGEMENT ==========")

        print("1. Add Course")
        print("2. View Course Details")
        print("3. View All Courses")
        print("4. View Students in a Course")
        print("5. Back")

        choice: int = int(input("Enter the chioce: "))
        if choice == 1:
            add_course(Courses)
        elif choice == 2:
            view_course_details(Courses)
        elif choice == 3:
            view_all_courses(Courses)
        elif choice == 4:
            view_students_in_a_course(Courses)
        elif choice == 5:
            return
        else:
            print("Invalid choice.")
           
def reports(Students,Professors,Courses):
    while True:
        print("========== REPORTS ==========")

        print("1. Students in a Course")
        print("2. Courses of a Professor")
        print("3. Students by Semester")
        print("4. Top GPA Students")
        print("6. Back")    

        choice: int = int(input("Enter the chioce: "))
        if choice == 1:
            view_students_in_a_course(Courses)
        elif choice == 2:
            view_courses_of_professor(Professors)
        elif choice == 3:
            students_by_semester(Students)
        elif choice == 4:
            top_student_according_to_GPA(Students)
        elif choice == 5:
            return
        else:
            print("Invalid choice.")
            
def professor_menu(Professors):
    while True:
        print("========== PROFESSOR ==========")

        print("1. View My Courses")
        print("2. View Students in My Courses")
        print("3. Assign Grade to Student")
        print("4. Back")
        choice: int = int(input("Enter the chioce: "))
        if choice == 1:
            view_courses_of_professor(Professors)
        elif choice == 2:
            view_students_of_professor(Professors)
        elif choice == 3:
            assign_grades_by_professor_to_student(Professors)
        elif choice == 4:
            return
        else:
            print("Invalid choice.")
   
def student_menu(Students,Courses):
    while True:
        print("========== STUDENT ==========")
        print("1. View My Details")
        print("2. Enroll in Courses")
        print("3. View My Courses")
        print("4. View My GPA")
        print("5. Back")
        choice: int = int(input("Enter the chioce: "))
        if choice == 1:
            view_student_details(Students)
        elif choice == 2:
            student_enroll_in_course(Students,Courses)
        elif choice == 3:
            view_courses_of_student(Students)
        elif choice == 4:
            print_student_gpa(Students)
        elif choice == 5:
            return
        else:
            print("Invalid choice.")
    
def administrator(Students,Professors,Courses):
    while True:
        print("========== ADMINISTRATOR ==========")
        print("1. Student Management")
        print("2. Professor Management")
        print("3. Course Management")
        print("4. Reports")
        print("5. Back")
        choice:int = int(input("Enter the chioce: "))
        if choice == 1:
            student_management(Students)
        elif choice == 2:
            professor_management(Professors,Courses)
        elif choice == 3:
            course_management(Courses)
        elif choice == 4:
            reports(Students,Professors,Courses)
        elif choice == 5:
            return
        else:
            print("Invalid choice.")

def menu():
    Students:list = list()
    Professors:list = list()
    Courses:list = list()
    while True:
        print("=" * 30 + "UNIVERSITY MANAGEMENT SYSTEM" + "=" * 30)
        print("1. Administrator")
        print("2. Professor")
        print("3. Student")
        print("4. Exit")
        print("\n")
        choice:int = int(input("Enter the chioce: "))
        if choice == 1:
            administrator(Students,Professors,Courses)
        elif choice == 2:
            professor_menu(Professors)
        elif choice == 3:
            student_menu(Students,Courses)
        elif choice == 4:
            return
        else:
            print("Invalid choice.")

def main():
    menu()
    print("Thanking you...")
    print("See you again.")     
       
if __name__=="__main__":
    main()




















# so The Flow will be like the course should be created first then
#          professor then professor has to enroll the course then it will immediatly add 
#          access the professor in to the course and verse-vice then only student get created then
#          it will also effect on the student but suppose student enrolled the course first 
#          before professor get assigned to this course after that professor is assigned for this course so it will automatically
#          refelect in student course list I think you can understand What I am tring to say   
