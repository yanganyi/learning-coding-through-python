# Python OOP

import datetime

# class
class Employee:

    #variables
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        # instances
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@abc.xyz"
        self.fullname = "{} {}".format(self.first,self.last)

        Employee.num_of_emps += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #classmethods
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Fat","Cat",1000000)
emp_2 = Employee("Skinny","Dog",1)

emp_str_1 = "Amy-Goh-70000"
emp_str_2 = "Ben-Tan-30000"
emp_str_3 = "Carol-Lee-50000"
new_emp_1 = Employee.from_string(emp_str_1)

print("Name: ",emp_1.fullname,"   Pay: S$",emp_1.pay,"   Email: ",emp_1.email)
print("Name: ",emp_2.fullname,"   Pay: S$",emp_2.pay,"   Email: ",emp_2.email)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.num_of_emps)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

my_date = datetime.date(2020,2,22)
print(Employee.is_workday(my_date))