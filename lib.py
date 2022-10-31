import numpy as np 
import matplotlib.pyplot as plt
import time

def dft(image):
    initialTime = time.time()
    rows, columns = image.shape
    final = np.zeros((rows, columns), complex)
    aux = np.zeros((rows, columns), complex)
    m = np.arange(rows)
    n = np.arange(columns)
    x = m.reshape((rows, 1))
    y = n.reshape((columns, 1))
    
    for row in range(0,rows):
        M1 = 1j*np.sin(-2*np.pi*y*n/rows) + np.cos(-2*np.pi*y*n/rows)
        aux[row] = np.dot(M1, image[row])
        
    for column in range(0,columns):
        M2 = 1j*np.sin(-2*np.pi*x*m/columns) + np.cos(-2*np.pi*x*m/columns)
        final[:,column] = np.dot(M2, aux[:,column])
    
    executionTime = time.time() - initialTime
    print('DFT time:', executionTime)
    return final

def idft(finalFunction):
    initialTime = time.time()
    rows, columns = finalFunction.shape
    final = np.zeros((rows, columns), complex)
    aux = np.zeros((rows, columns), complex)
    m = np.arange(rows)
    n = np.arange(columns)
    x = m.reshape((rows, 1))
    y = n.reshape((columns, 1))
    
    for row in range(0,rows):
        M1 = 1j*np.sin(-2*np.pi*y*n/rows) + np.cos(-2*np.pi*y*n/rows)
        aux[row] = np.linalg.solve(M1,finalFunction[row])
        
    for column in range(0,columns):
        M2 = 1j*np.sin(-2*np.pi*x*m/columns) + np.cos(-2*np.pi*x*m/columns)
        final[:,column] = np.linalg.solve(M2,aux[:,column])

    executionTime = time.time() - initialTime
    print('IDFT time:', executionTime)
    return final

def infiniteMeshFilter(image, kernel):
    initialTime = time.time()
    size = image.shape
    M = size[0]-1 # M = 199
    N = size[1]-1 # N = 199
    
    dst = np.zeros((N+1,N+1))

    K = M+2 # K = 201
    image2           = np.zeros((K+1, K+1))
    image2[1:K,1:K]  = image
    image2[0,1:K]    = image[M,:] 
    image2[K,1:K]    = image[0,:] 
    image2[1:K,0]    = image[:,N] 
    image2[1:K,K]    = image[:,0] 
    image2[0,0]      = image[M,N] 
    image2[0,K]      = image[M,0] 
    image2[K,0]      = image[0,N] 
    image2[K,K]      = image[0,0]

    # Filtering
    for i in range(1,K):
        for j in range(1,K):        
            dst[i-1,j-1]=np.sum(np.sum(np.multiply(image2[i-1:i+2,j-1:j+2],kernel)))

    executionTime = time.time() - initialTime
    print('FBR time:', executionTime)
    return dst

def sameBorderFilter(image, kernel):
    size = image.shape
    N = size[1]-1
    dst = np.zeros((N+1,N+1))
    initialTime = time.time()
    # Filtro cru
    for i in range(1,N):
        for j in range(1,N):        
            dst[i,j]=np.sum(np.sum(np.multiply(image[i-1:i+2,j-1:j+2],kernel)))
            executionTime = time.time() - initialTime
    print('Execution time (seconds):', executionTime)
    image[1:N,1:N] = dst[1:N,1:N]

    return image

def switches0by1(matrix, fourier_image):
    rows, columns = matrix.shape
    flag = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i,j]==0j: 
                print(fourier_image[i,j])
                matrix[i,j]=1
                flag = 1
    if flag==0:
        print("No switching was necessary")
    return matrix
