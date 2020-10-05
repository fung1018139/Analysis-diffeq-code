import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)

M=100#時間の分割数
N=100#変位の分割数
T=10#時間の上限
X=2#変位の上限
DELTA_X=X/N
DELTA_T=T/M
c=3
a=(DELTA_T*c)/DELTA_X
U=[[] for i in range(M)]
def F(x):
    return x**2
for i in range(N):
    U[0].append(F(i*DELTA_X))

for n in range(M-1):
    U[n+1].append(0)#境界条件
    for j in range(1,N-1):
        U[n+1].append((1+a)*U[n][j]-a*U[n][(j+1)])
    U[n+1].append(0)#境界条件

x=np.arange(0,X,DELTA_X)
t=np.arange(0,T,DELTA_T)
x,t=np.meshgrid(x,t)
Ux=np.array(U)
ax.plot_surface(x,t,Ux)
plt.show()



