import numpy as np
import matplotlib.pyplot as plt


#LSM local maxima scalogram

def LSM(sig):
    len_sig=len(sig)
    L=int(np.ceil(len_sig/2))
    win_size=2*np.linspace(1,L,L)
    M=np.zeros([L,len_sig])
    for k in range(1,L+1):
        for i in range(k+2,len_sig-k+2):
            if sig[i-2]>sig[i-k-2] and sig[i-2]>sig[i+k-2]:
                pass
            else:
                M[k-1,i-1]=np.random.rand(1)[0]+1
    return M,L

def Row_wise(M):
    return np.sum(M,1).tolist()

def Reshape_M(M,L):
    y=Row_wise(M)
    gam=y.index(min(y))
    M[gam+1:,:]=0
    return M,gam

def Col_wise(sig):
    M,L=LSM(sig)
    M,gam=Reshape_M(M,L)
    delta=1/gam*np.sum(np.abs(M-np.mean(M,0)),0)
    p=np.where(delta==0)
    return p



def main():
    N = 1000
    x = np.linspace(0, 200, N)
    y = 2 * np.cos(2 * np.pi * 300 * x) \
        + 5 * np.sin(2 * np.pi * 100 * x) \
        + 4 * np.random.randn(N)

    plt.plot(range(len(y)), y)
    px = Col_wise(y)
    plt.scatter(px, y[px], color="red")
    plt.savefig('./image/fig1.jpg')
    plt.show()


if __name__=="__main__":
    main()

