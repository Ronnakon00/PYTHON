import matplotlib.pyplot as plt

product1 = [10,20,30,40,50]
product2 = [15,30,10,20,60]
month = [1,2,3,4,5]

data = {'size':20,'color':'blue','backgroundcolor':'c'}
plt.xlabel('Month',data)
plt.ylabel('Sales',size=15,color='red',backgroundcolor='black')

plt.plot(month,product1,'bo-')
plt.plot(month,product2,color='r',marker = '|',linestyle='--')

#plt.savefig('export1.png')
#plt.savefig('export2.png',transparent=True)

plt.title('top sale 2020',data,loc='left')

plt.text(2,10,'Point',size=15,color='red')

plt.show()