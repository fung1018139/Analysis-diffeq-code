import numpy as np
import matplotlib.pyplot as plt

#波動方程式の数値シミュレーション vol2
#[1]
M=50#時間の分割数
N=20#変位の分割数
T=1
DELTA_X=(1/N)
DELTA_T=(T/M)
a=(DELTA_T**2)/(DELTA_X**2)

if (a)<=1:
    #[2]
    U=[[] for i in range(M+1)]#配列の初期化0からMまでの配列※重要！！

    #U(x,0)
    def F(t,x):
        #np.exp(-((x-2)**2)*10)*np.exp(-((t-2)**2)*10)*2
        return x*(2-x)

    #∂U∂x
    def f(t,x):
        h=0.001
        return (F(t+h,x)-F(t-h,x))/(2*h)

    #初期条件その１
    #U0
    for j in range(N):
        U[0].append(F(0,j*DELTA_X))
    U[0].append(U[0][-1])
    #U1
    U[1].append(0)
    for j in range(1,N):
        U[1].append(U[0][j]+DELTA_T*f(0,j*DELTA_X)+(a/2)*(U[0][j+1]-2*U[0][j]+U[0][j-1]))
    U[1].append(U[1][-1])

    for n in range(1,M):
        U[n+1].append(0)
        for j in np.arange(1,N):
            U[n+1].append(2*U[n][j]-U[n-1][j]+a*(U[n][j+1]-2*U[n][j]+U[n][j-1]))
        U[n+1].append(U[n+1][-1])
    
        #配列を作る
    U0=[U[i][10] for i in range(M+1)]
    U=np.array(U)
    t=np.linspace(0,T,M+1)
    x=np.linspace(0,1,N+1)
    # for i in range(10):
    #     plt.plot([0.1*i,0.1*i],[0,0.8],c='b')
    
    for i in range(0,len(U0),5):
        print(t[i],U0[i])
    plt.scatter(t,U0)
    plt.grid()

    from mpl_toolkits.mplot3d import Axes3D
    #グラフの枠を作っていく
    fig = plt.figure()
    ax = Axes3D(fig)
    x1,t1=np.meshgrid(x,t)
    ax.set_xlabel("x")
    ax.set_ylabel("t")  
    ax.scatter(x[10],t,U0)#x=0.5に対してグラフの作成
    ax.scatter3D(x1,t1,U)

    plt.show()

else:
    print("Not Stable!")
