import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

#[1]
M=100
N=50
T=1
DELTA_X=(1/N)#1/N
DELTA_T=(T/M)#T/M

a=(DELTA_T)/((DELTA_X)**2)

#[2]
U=[[] for i in range(M+1)]

def border(x):
    if (0<=x and x<=1/2):
        return x  
    else:
        return 1-x
#境界条件
for j in range(N+1):
    U[0].append(border(j*DELTA_X))


#ここから連立方程式を作成して解く
#一行目
a1=[1+2*a,-a]
for i in range(N-3):
    a1.append(0)
#二行目~N-2行目
a0=[-a,1+2*a,-a]
def mm(m):
    am=[]
    for i in range(m-2):
        am.append(0)
    for i in range(len(a0)):
        am.append(a0[i])
    for i in range(N-3-(m-1)):
        am.append(0)
    return am
#N-1行目
al=[]
for i in range(len(a1)):
    al.append(a1[-1-i])

#係数行列を作る
A=[]
A.append(a1)
for i in np.arange(2,N-1):
    A.append(mm(i))
A.append(al)

#Uには元々0~Nまでの11個が格納されている
Us=[U[0][1:N]]
#一行目からN−１行目までの計算を行う
for i in range(M):
    Us.append(np.linalg.solve(A,Us[i]))
#UsにはUの1~N-1までの要素が入っている
#初期条件
for i in range(len(Us)):
    Us[i]=list(Us[i])
    Us[i].insert(0,0)
    Us[i].append(0)
#ここまでで陰公式を終え、配列を作成した


#グラフの描画
Us=np.array(Us)
x=np.linspace(0,1,N+1)
t=np.linspace(0,T,M+1)
s,q=np.meshgrid(x,t)
ax.set_xlabel("x")
ax.set_ylabel("t")
ax.plot_surface(s,q,Us)
#DELTA_T=0.02[t][x]
print(Us[4][25])
#plt.show()

