import matplotlib.pyplot as plt
room = ['A','B','C']
boys = [10,15,5]
girls = [20,7,15]

plt.stackplot(room,boys,girls,labels=['boys','girls'],colors=['blue','pink'])
plt.legend()
plt.show()