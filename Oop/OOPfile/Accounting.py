from Employee import Employee
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