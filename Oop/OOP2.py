class Employee:
    _maxSalary = 999999
    _minSalary = 10000
    def __init__(self,name,salary,department):
        self.__name = name
        self.__salary = salary
        self.__department = department   

    def _showData(self):
        print(self.__name)
        print(self.__salary)
        print(self.__department)

class Accounting(Employee):
    __departmentName = "Accounting"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)

class Programmer(Employee):
    __departmentName = "Programmmer"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)

class Saler(Employee):
    __departmentName = "Saler"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)

account = Accounting("Ronnakon",50000)
account._showData()
