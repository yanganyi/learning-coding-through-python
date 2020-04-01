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

# class Developer inherits everything from Employee class
# changes is subclass does not affect parent class
class Developer(Employee):
    raise_amount = 1.10
    def __init__(self,first,last,pay,prog_lang):
        # super stands for the superior parent class
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang



class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        # super stands for the superior parent class
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname)



emp_1 = Employee("Fat","Cat",1000000)
emp_2 = Employee("Skinny","Dog",1)

dev_1 = Developer("Fat","Cat",1000000,'Python')
dev_2 = Developer("Skinny","Dog",1,'C++')

man_1 = Manager("Fat","Cat",1000000000,[dev_1])
man_2 = Manager("Skinny","Dog",1000000000,[dev_2])

emp_str_1 = "Amy-Goh-70000"
emp_str_2 = "Ben-Tan-30000"
emp_str_3 = "Carol-Lee-50000"
new_emp_1 = Employee.from_string(emp_str_1)

# print("Name: ",emp_1.fullname,"   Pay: S$",emp_1.pay,"   Email: ",emp_1.email)
# print("Name: ",emp_2.fullname,"   Pay: S$",emp_2.pay,"   Email: ",emp_2.email)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.__dict__)
# print(Employee.__dict__)
# print(Employee.num_of_emps)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# Employee.set_raise_amount(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# my_date = datetime.date(2222,2,22)
# print(Employee.is_workday(my_date))
#
#
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(dev_1.prog_lang)
# print(dev_2.prog_lang)
#
#
# print(man_1.print_emps())
# man_1.add_emp(dev_2)
# print(man_1.print_emps())
# man_1.remove_emp(dev_1)
# print(man_1.print_emps())
#
#
# print(isinstance(man_1,Manager))
# print(isinstance(man_1,Employee))
# print(isinstance(man_1,Developer))
# print(issubclass(Manager,Employee))
# print(issubclass(Developer,Employee))
# print(issubclass(Manager,Developer))
# print(issubclass(Developer,Manager))
