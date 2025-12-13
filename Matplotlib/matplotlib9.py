import matplotlib.pyplot as plt

course = ['python','java','c#']
score = [80,75,50]
c = ['green','orange','blue']

plt.xlabel('Course')
plt.ylabel('Score')
plt.title('Score midterm')
plt.bar(course,score,color=c,width=0.6,edgecolor='red',linewidth=3)

plt.show()