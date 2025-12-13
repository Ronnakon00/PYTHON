import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1.2,3,2.3,4.5,4.3]
sizes = [100,200,50,10,60]
color = ['blue','red','pink','purple','cyan']
plt.scatter(x,y,s=sizes,c=color)

plt.show()