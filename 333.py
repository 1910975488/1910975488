import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,20)
x1=np.linspace(0,10,10)
X=[2,1.5,1,0.5]
y1=[]
for i in range(32):
      y1.append(X[i%4])
fig=plt.figure('16010140048')

plt.subplot(323)
y3=[1,0,0,0,0,0,0,0,0]
plt.stem(y3)
plt.grid(True)
plt.title('chongji')

plt.show()