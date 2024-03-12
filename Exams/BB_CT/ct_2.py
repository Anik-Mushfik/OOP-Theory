from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass
    
    def __str__(self):
        return f"Employee Name: {self.name} \nEmployee ID: {self.employee_id}"


class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return f"Salary: {self.hourly_rate * self.hours_worked}"
    

class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def calculate_salary(self):
        return f"Salary: {self.salary}"
        

class CommissionedEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, commission_rate, sales):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
        self.commission_rate = commission_rate
        self.sales = sales

    def calculate_salary(self):
        return f"Salary: {self.base_salary + (self.commission_rate * self.sales)}"


# Hourly employee-
emp_1 = HourlyEmployee("jodu", 13441, 100, 25)
print(emp_1)
print(emp_1.calculate_salary())

# Commissioned Employee-
emp_2 = CommissionedEmployee("Modu", 29437, 10000, 0.25, 5000)
print(emp_2)
print(emp_2.calculate_salary())

# Sallaried Employee -
emp_3 = SalariedEmployee("Kodu", 29734, 20000)
print(emp_3)
print(emp_3.calculate_salary())