from Employee import Employee
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