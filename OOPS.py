
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary
Employee_1=Employee("liji","95000")
print("Employee Name:",Employee_1.get_name())
print("Employee Salary:",Employee_1.get_salary())
