import numpy as np

# 三重対角行列のLU分解
# A=[[1,1,0,0],[1,2,6,0],[0,3,1,2],[0,0,2,1]]
# y=[1,2,3,4]
# if len(y)==len(A):
#     a=[A[i][i] for i in range(len(A))]
#     b=[A[i+1][i] for i in range(len(A)-1)]
#     c=[A[i][i+1] for i in range(len(A)-1)]
#     #LU分解
#     d=[a[0]]
#     l=[]
#     N=len(A)
#     for i in range(1,N):
#         l.append(b[i-1]/d[i-1])
#         d.append(a[i]-l[i-1]*c[i-1])
#     L=np.diag([l[i] for i in range(len(l))],k=-1)+np.eye(N)
#     U=np.diag([d[i] for i in range(len(d))])+np.diag([c[i] for i in range(len(c))],k=1)
#     #任意の三重対角行列のLU分解
#     #前進代入
#     z=[y[0]]
#     for i in range(1,N):
#         z.append(y[i]-l[i-1]*z[i-1])
#     #後退代入
#     #いったん逆に代入する。
#     x=[0]*len(y)
#     x[N-1]=z[N-1]/d[N-1]
#     for i in range(1,N):
#         x[N-1-i]=(z[N-1-i]-c[N-1-i]*x[N-i])/d[N-1-i]
#     print(x)

#任意の行列についてのLU分解のアルゴリズム
A=[[1,0,0],[1,1,1],[0,-1,1]]
y=[1,2,3]
N=len(A)
u=[[] for i in range(N)]
l=[[] for i in range(N)]

for j in range(N):
    for j1 in np.arange(j,-1,-1):
        S=0
        for j2 in range(j-j1):
            S+=l[j2][j-j2-j1-1]*u[j][j2]
        u[j].append(A[j-j1][j]-S)
    for i in range(j+1,N):
        T=0
        for s in range(j):
            T+=(l[s][i-s-1]*u[j][s])
        l[j].append((A[i][j]-T)/u[j][j])
        
#LU分解はできている。

#前進代入
z=[0]*len(y)
z[0]=y[0]
for i in range(1,N):
    S=0
    for i1 in range(i):
        S+=l[i-(i1+1)][0]*z[i1]
    z[i]=y[i]-S
#後退代入
x=[0]*len(z)
x[N-1]=z[N-1]/u[N-1][N-1]
for i in range(N-2,-1,-1):
    S=0
    for k in range(i+1,N):
        S+=u[k][i]*x[k]
    x[i]=(z[i]-S)/u[i][i]
print(x)

