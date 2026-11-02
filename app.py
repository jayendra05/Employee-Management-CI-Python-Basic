employees = [
    {"id": 1, "name": "Rahul", "department": "IT"},
    {"id": 2, "name": "Amit", "department": "HR"},
    {"id": 3, "name": "Priya", "department": "Finance"}
]


# Function 1: Display all employees
def get_employees():
    return employees


# Function 2: Search employee by ID
def get_employee_by_id(employee_id):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return None


# Function 3: Add a new employee
def add_employee(employee_id, name, department):

    employee = {
        "id": employee_id,
        "name": name,
        "department": department
    }

    employees.append(employee)

    return employee


# Main program
if __name__ == "__main__":

    print("Employee Management System")

    print("\nAll Employees:")
    print(get_employees())

    print("\nSearch Employee:")
    print(get_employee_by_id(1))

    print("\nAdding New Employee:")
    print(add_employee(4, "Jay", "Cloud"))

    print("\nUpdated Employee List:")
    print(get_employees())