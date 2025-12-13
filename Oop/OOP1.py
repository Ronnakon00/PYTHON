class Employee:
    _maxSalary = 999999
    _minSalary = 10000
    def __init__(self,name,salary,department):
        self.__name = name
        self.__salary = salary
        self.__department = department   

    def _showData(self):
        print(self.getName())
        print(self.getSalary())
        print(self.getDepratment())

    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary

    def setDeoartment(self,newdepartment):
        self.__department = newdepartment

    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def getDepratment(self):
        return self.__department
    
obj1 = Employee("Ronnakon",40000,"Programmer")
# obj2 = Employee("KLuay",50000,"Enginear")
# obj3 = Employee("Peath",30000,"Saler")

print(Employee._minSalary)