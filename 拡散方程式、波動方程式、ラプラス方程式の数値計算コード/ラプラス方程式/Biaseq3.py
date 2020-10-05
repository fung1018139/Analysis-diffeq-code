import numpy as np
import math
import matplotlib.pyplot as plt


N=10#x方向の分割数
M=N#y方向の分割数。本来は考えるべきだが、疲れたので俺はx方向のみにします
h=(1/N)
k=(1/M)
π=math.pi
#N、Mはそれぞれx方向y方向の分割数

A=4*np.eye(N-1)+(-1)*np.eye(N-1,k=1)+(-1)*np.eye(N-1,k=-1)
B=-1*np.eye(N-1)
O=np.zeros_like(A)
A=list(A)
B=list(B)
O=list(O)

#係数行列の作成
#係数行列をLapras＿Aとする
Lapras_A=[]

for i in range(N-1):    
    L=np.append(A[i],B[i])
    for j in range((N-1)**2-2*(N-1)):
        L=np.append(L,0)
    L=list(L)
    Lapras_A.append(L)

for k in range(N-3):
    #上からk段目のBAB
    for i in range(N-1):
        P=(np.append(B[i],A[i]))
        P=(np.append(P,B[i]))
        #前に追加
        for s in range(k):
            P=np.insert(P,0,O[k])
        LEN=(len(P))
        #後ろに追加
        for j in range(((N-1)**2)-LEN):
            P=(np.append(P,0))
        P=list(P)
        Lapras_A.append(P)

for i in range(N-1):
    S=np.append(B[i],A[i])
    for j in range((N-1)**2-2*(N-1)):
        S=np.insert(S,0,0)
    Lapras_A.append(S)

def delta1(x):
    return x*(1-x)
def delta2(y):
    return y*(1-y)
#境界条件の挿入
U=[[1,0] for i in range(1,N)]
U.insert(0,[1]+[1]*(N))
U.append([1]+[i for i in range(N)])


#fは連立方程式のためのVector。Ax=bのb
f1=[U[0][1]+U[1][0],U[-1][1]+U[-2][0]]
for i in range(2,N-2+1):
    f1.insert(1+i,U[i][0])

#fj
fj=[]
for k in range(2,N-2+1):
    fjp=[U[0][k-1],U[-1][k-1]]

    for i in range(2,N-2+1):
        fjp.insert(i-1,0)
    fj.append(fjp)


#fN-1
fn1=[U[0][-2]+U[1][-1],U[-1][-2]+U[-2][-1]]
for i in range(2,N-2+1):
    fn1.insert(1+i,U[i][-1])

f=[]
for i in range(len(f1)):
    f.append(f1[i])
for j in range(2,N-2+1):
    for i in range(len(fj[j-2])):
        f.append(fj[j-2][i])
for i in range(len(fn1)):
    f.append(fn1[i])

#import pandas as pd
# Lapras=pd.DataFrame(Lapras_A)
# Lapras.to_csv("/Users/nakamurayuma/Desktop/Laplas.csv",header=False,index=False)

#解を求める
p=np.linalg.solve(Lapras_A,f)

for i in range(1,N):
    for j in range(1,N):
        U[i].insert(j,p[i-1+(3*(j-1))])
#Singular matrixが出る時は解が求まらない→逆行列が存在しない
#グラフの描画
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)


Ux=np.array(U)
x=np.linspace(0,1,N+1)
y=np.linspace(0,1,M+1)
x,y=np.meshgrid(x,y)
ax.plot_surface(x,y,Ux)
plt.show()
 
