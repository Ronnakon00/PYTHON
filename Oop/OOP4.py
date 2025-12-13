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

    def getincome(self):
        return self.__salary *12

    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {} , รายได้ต่อปี = {}".format(self.__name,self.__department,self.__salary,self.getincome()))
    
class Accounting(Employee):
    __departmentName = "Accounting"
    def __init__(self,name,salary,age): 
        super().__init__(name,salary,self.__departmentName)
        self.__age = age
    
    def _showData(self):
        super()._showData()
        print(self.__age,end="\n\n")

    def __str__(self):
        return(super().__str__()+" , อายุ = {}".format(self.__age))


class Programmer(Employee):
    __departmentName = "Programmmer"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentName)
        self.__experience = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print(self.__experience)
        print(self.__skill,end="\n\n")

    def __str__(self):
        return(super().__str__()+" , ประสบการณ์ = {} , สกิล = {}".format(self.__experience,self.__skill))

class Saler(Employee):
    __departmentName = "Saler"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData()
        print(self.__area,end="\n\n")

    def __str__(self):
        return(super().__str__()+" , สถานที่ = {}".format(self.__area))
    
print("-----------------------------------------------------------------------------------------------------")
account = Accounting("Ronnakon",50000,12)
print(account.__str__())
print("-----------------------------------------------------------------------------------------------------")
program = Programmer("Thammakhun",70000,4,"game dev")
print(program.__str__())
print("-----------------------------------------------------------------------------------------------------")
sale = Saler("Kluay",60000,"rayong")
print(sale.__str__())
print("-----------------------------------------------------------------------------------------------------")
