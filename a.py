import numpy as np
import matplotlib.pyplot as plt
import seaborn as srs
x = ['Shirt','Pants','Shorts','Shoes']
y = [1000,1200,800,200]

plt.barh(x,y)
plt.title('Sale')
plt.xlabel('Catagory')
plt.ylabel('Price')
plt.show()