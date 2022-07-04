# NOTE: This demonstrates encapsulation in that we can create
# classes and methods together in the same struture.

class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # instance members
        self.name = name
        self.__salary = salary  # PRIVATE
        self.project = project

    def data(self):
        """
        Method to return the employees attributes as data.
        :return:  A dict with the employees data..
        """
        return {'name': self.name, 'salary': self.__salary, 'project': self.project}

    def show(self):
        """
        Method to print some info about the meployee.
        :return:  Prints out the name and salary.
        """
        # accessing public data member
        print(f"Name: {self.name} Salary: {self.__salary}")

    def work(self):
        """
        Method to display employees work.
        :return:  A dict with the employees name and current project..
        """
        print(f"{self.name} is working on {self.project}")


if __name__ == "__main__":
    # creating object instance of a class
    emp = Employee('Jessa', 8000, 'NLP')

    # calling public methods of the class
    emp.data()
    emp.show()
    emp.work()
    # try printing a private variable directly.
    try:
        print(emp.__salary)
    except:
        print("Salary is private")
