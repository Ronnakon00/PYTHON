import matplotlib.pyplot as plt
student = [10,20,40,30,60]
course = ['PHP','java','python','c','c#']
color = ['blue','red','pink','purple','cyan']
exp=[1,0,0,0,0]
plt.pie(student,labels=course,autopct='%.2f%%',colors=color,shadow=True,explode=exp,startangle=10)
plt.show()
