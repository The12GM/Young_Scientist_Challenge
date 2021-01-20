import numpy as np
print("Euclidean space is the fundamental space of classical geometry. Originally it was the three-dimensional space of Euclidean geometry, but in modern mathematics there are Euclidean spaces of any nonnegative integer dimension,including the three-dimensional space and the Euclidean plane (dimension two).")
print("\nEuclidean distance matrix is an n×n matrix representing the spacing of a set of n points in Euclidean space/norm.")
a=np.array([[1,2,3],[2,3,4],[0,1,2]])
print("Array A is equal to",a)
b=np.array([[1,2,3],[4,3,2]])
print("Array B is eqaul to",b)
m=a.shape[0]
print("M is ",m)
n=b.shape[0]
print("N is",n)
a_d=(a*a).sum(axis=1).reshape((m,1))*np.ones(shape =(1,n))
print("a_d is equal to",a_d)
b_d=(b*b).sum(axis=1)*np.ones(shape=(m,1))
print("b_d is equal to",b_d)
d_squared =  a_d + b_d -2*a.dot(b.T)
print("d_squared is = to ",d_squared)
def dis_matrix(a,b,squared=False):
    m=a.shape[0]
    n=b.shape[0]
    assert a.shape[1]==b.shape[1], f"The number of components for vectors in A \{a.shape[1]} does not match that of B {b.shape[1]}!"
    a_d=(a*a).sum(axis=1).reshape((m,1))*np.ones(shape =(1,n))
    b_d=(b*b).sum(axis=1)*np.ones(shape=(m,1))
    d_squared =  a_d + b_d -2*a.dot(b.T)
    
    if squared==False:
         zero_mask = np.less(d_squared, 0.0)    
         d_squared[zero_mask]= 0.0
         return d_squared
    return d_squared
print("This the final answer to the euclidean-distance-matrix-calculations is",dis_matrix(a, b))