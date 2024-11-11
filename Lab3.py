class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        for emp in self.employees:
            print(emp)

    def remove_employees_by_age_range(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary(self, name, new_salary):
        employee = self.find_employee_by_name(name)
        if employee:
            employee.salary = new_salary
        else:
            print("Employee not found")


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def add_new_employee(self):
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        salary = float(input("Enter employee salary: "))
        employee = Employee(name, age, salary)
        self.manager.add_employee(employee)

    def display_all_employees(self):
        self.manager.list_employees()

    def remove_employees_in_age_range(self):
        min_age = int(input("Enter minimum age: "))
        max_age = int(input("Enter maximum age: "))
        self.manager.remove_employees_by_age_range(min_age, max_age)

    def update_employee_salary(self):
        name = input("Enter employee name: ")
        new_salary = float(input("Enter new salary: "))
        self.manager.update_salary(name, new_salary)


if __name__ == "__main__":
    frontend = FrontendManager()
    while True:
        print("\n1. Add Employee\n2. List Employees\n3. Remove Employees by Age\n4. Update Salary\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            frontend.add_new_employee()
        elif choice == '2':
            frontend.display_all_employees()
        elif choice == '3':
            frontend.remove_employees_in_age_range()
        elif choice == '4':
            frontend.update_employee_salary()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
