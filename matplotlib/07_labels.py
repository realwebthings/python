import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

x1 = np.linspace(0, 20, 100)
y1 = np.cos(x1)

fontD = {'family':'serif', 'color':'darkred', 'size':15, 'alpha':0.5, 'weight':'bold'}
plt.xlabel('x',fontdict=fontD)
plt.ylabel('y', fontdict=fontD)

plt.title('Sine and Cosine', fontdict=fontD)
# plt.title('Sine and Cosine', fontsize=20, color='darkred', alpha=0.5)
plt.plot(x, y, marker='o', label='sin(x)')
plt.plot(x1, y1, marker='s', label='cos(x)')
plt.legend()
plt.show()