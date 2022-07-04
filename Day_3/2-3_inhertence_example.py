# Parent class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Inside Person class')
        print('Name:', name, 'Age:', age)


# Parent class 2
class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)


# Child class
class Employee(Person, Company):
    def __init__(self, name, age, salary, skill, company_name, location):
        Person.__init__(self, name, age)
        Company.__init__(self, company_name, location)
        self.salary = salary
        self.skill = skill
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)


if __name__ == '__main__':
    # Create object of Employee
    emp_12643 = Employee(name='Bob Smith',
                         age=25,
                         salary=136000,
                         skill='NLP',
                         company_name='Google',
                         location='Atlanta, GA')
