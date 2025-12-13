from Employee import Employee
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