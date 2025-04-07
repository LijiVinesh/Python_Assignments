#
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def get_name(self):
#         return self.name
#
#     def get_salary(self):
#         return self.salary
# Employee_1=Employee("liji","95000")
# print("Employee Name:",Employee_1.get_name())
# print("Employee Salary:",Employee_1.get_salary())

class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"Course Code: {self.course_code}, Name: {self.course_name}, Credit Hours: {self.credit_hours}"

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        # Initialize the parent class (Course)
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        core_info = "Required for major" if self.required_for_major else "Not required for major"
        return f"{super().__str__()}, {core_info}"

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        # Initialize the parent class (Course)
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return f"{super().__str__()}, Elective Type: {self.elective_type}"

# Create instances
course1 = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
course2 = ElectiveCourse("MATH210", "Calculus II", 4, "technical")

# Print courses
print(course1)
print(course2)