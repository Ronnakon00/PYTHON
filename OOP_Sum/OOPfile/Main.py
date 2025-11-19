from Accounting import Accounting
from Programmer import Programmer
from Saler import Saler
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
