import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy as sp
from scipy import linalg

def img_cps(S,n):
    #nz_s=np.count_nonzero(S)
    print("Nonzero of sigma:",np.count_nonzero(S))
    for i in range(len(S)):
        if i in range(n):
            S[i]=S[i]
        else:
            S[i]=0
    S = sp.linalg.diagsvd(S, 800, 1000)
    return S

def SVD(r,g,b,n):
    #RED
    Ur,S,Vr=sp.linalg.svd(r)
    Sr=img_cps(S,n)
    r=np.dot(Ur,np.dot(Sr,Vr))
    #GREEN
    Ug,S,Vg=sp.linalg.svd(g)
    Sg=img_cps(S,n)
    g=np.dot(Ug,np.dot(Sg,Vg))
    #blue
    Ub,S,Vb=sp.linalg.svd(b)
    Sb=img_cps(S,n)
    b=np.dot(Ub,np.dot(Sb,Vb))
    return r,g,b

if __name__ == "__main__":

    img=mpimg.imread('eco-pot.jpg')
    [r,g,b] = [img[:,:,i] for i in range(3)]

    fig = plt.figure(1)
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()

    #for n=30
    [r,g,b]=SVD(r,g,b,30)
    img[:,:,0]= r
    img[:,:,1]= g
    img[:,:,2]= b
    fig = plt.figure(2)
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()
    
    img=mpimg.imread('eco-pot.jpg')
    [r,g,b] = [img[:,:,i] for i in range(3)]
    
    #for n=200
    [r,g,b]=SVD(r,g,b,200)
    img[:,:,0]= r
    img[:,:,1]= g
    img[:,:,2]= b
    fig = plt.figure(3)
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()