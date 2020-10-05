import numpy as np
import matplotlib.pyplot as plt

#ガウスの消去法
#問題設定
A=[[1,2s],[2,3]]
y=[1,1]
N=len(A)



#前進消去
for k in range(0,N):
    #部分ピボット
    Max=abs(A[k][k])
    for i in range(k+1,N):
        if Max<abs(A[k][i]):
            Max=abs(A[k][i])
    
    for l in range(k+1,N):
        if (Max==A[k][l]):
            A[k][k:N+1],A[l][k:N+1]=A[l][k:N+1],A[k][k:N+1]

            y[k],y[l]=y[l],y[k]
    for i in range(k+1,N):
        a=A[i][k]/A[k][k]
        for j in range(k+1,N):
            A[i][j]=A[i][j]-a*A[k][j]
        y[i]=y[i]-a*y[k]

#後退代入
x=[0]*N
x[N-1]=(y[N-1])/A[N-1][N-1]
for k in range(2,N+1):
    #シグマ計算
    SUM=0
    for i in np.arange(k-1,0,-1):
        SUM+=A[N-k][N-i]*x[N-i]
    x[N-k]=(y[N-k]-SUM)/A[N-k][N-k]
print(x)

