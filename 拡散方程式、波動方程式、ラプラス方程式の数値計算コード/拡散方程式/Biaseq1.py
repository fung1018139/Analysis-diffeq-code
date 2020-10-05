import numpy as np
import matplotlib.pyplot as plt
import math 

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)

π=math.pi
#[1]格子を作る条件や刻みはば
M=10000
N=20
T=1
DELTA_X=(1/N)#1/N
DELTA_T=(T/M)#T/M

a=(DELTA_T)/((DELTA_X)**2)
if (a<=0.5):
    print("stable")

#plotのための配列準備
#[2]
U=[[] for i in range(M+1)]
#初期条件
def border(x):
    return x*(1-x)
for j in range(N+1):
    U[0].append(border(j*DELTA_X))

#差分法
#[3]
for n in range(M):
    U[n+1].append(0)
    for j in np.arange(1,N):
        U[n+1].append(a*U[n][j+1]+(1-2*a)*U[n][j]+a*U[n][j-1])
    U[n+1].append(0)
print(a)
#グラフの描画
Ux=np.array(U)
x=np.linspace(0,1,N+1)
t=np.linspace(0,T,M+1)
x,t=np.meshgrid(x,t)
ax.set_xlabel("x")
ax.set_ylabel("t")
ax.plot_surface(x,t,Ux)
plt.plot([0,0],[1.0,1.0])
plt.show()
