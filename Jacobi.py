import numpy as np

A=[[5,4],[2,3]]
y=[13,8]

N=len(A)
#反復回数
MAX_T=100
X=[[] for i in range(MAX_T)]
X.insert(0,[0,0])
#ヤコビ法のための反復
i=0
while i<(MAX_T):
    j=0
    while j<N:
        S1=0
        for k in range(j):
            S1+=A[j][k]*X[i][k]
        S2=0
        for l in range(j+1,N):
            S2+=A[j][l]*X[i][l]
        S=S1+S2
        X[i+1].append((1/A[j][j])*(y[j]-S))
        print()
        print(X[i+1][j]-X[i][j])
        j+=1
    i+=1

# A=np.matrix(A)
# y=np.matrix(y).T
# S=np.linalg.solve(A,y)
# print(S)