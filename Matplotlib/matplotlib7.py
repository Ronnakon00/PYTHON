import matplotlib.pyplot as plt

age = [18,17,20,18,20,15,20,24,18,20,15,10,20,40,30,20,10,15,20,30]

plt.xlabel('Age')
plt.ylabel('Count')
plt.hist(age)
plt.title('Total age')

plt.show()