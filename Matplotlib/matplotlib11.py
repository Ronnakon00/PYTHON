import matplotlib.pyplot as plt
room = ['A','B','C']
boys = [10,15,5]
girls = [20,7,15]

plt.bar(room,boys,label='boys',color='blue')
plt.bar(room,girls,bottom=boys,label='girls',color='red')
plt.legend()
plt.show()