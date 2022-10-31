import numpy as np 
import matplotlib.pyplot as plt
import time

def dft(imagem):
    tempo_inicial = time.time()
    linhas, colunas = imagem.shape
    final = np.zeros((linhas, colunas), complex)
    aux = np.zeros((linhas, colunas), complex)
    m = np.arange(linhas)
    n = np.arange(colunas)
    x = m.reshape((linhas, 1))
    y = n.reshape((colunas, 1))
    
    for linha in range(0,linhas):
        
        M1 = 1j*np.sin(-2*np.pi*y*n/linhas) + np.cos(-2*np.pi*y*n/linhas)
        aux[linha] = np.dot(M1, imagem[linha])
        
    for coluna in range(0,colunas):
        
        M2 = 1j*np.sin(-2*np.pi*x*m/colunas) + np.cos(-2*np.pi*x*m/colunas)
        final[:,coluna] = np.dot(M2, aux[:,coluna])
    tempo_execucao = time.time() - tempo_inicial
    print('DFT time:', tempo_execucao)
    return final

def idft(transformada):
    tempo_inicial = time.time()
    linhas, colunas = transformada.shape
    final = np.zeros((linhas, colunas), complex)
    aux = np.zeros((linhas, colunas), complex)
    m = np.arange(linhas)
    n = np.arange(colunas)
    x = m.reshape((linhas, 1))
    y = n.reshape((colunas, 1))
    
    for linha in range(0,linhas):
        
        M1 = 1j*np.sin(-2*np.pi*y*n/linhas) + np.cos(-2*np.pi*y*n/linhas)
        aux[linha] = np.linalg.solve(M1,transformada[linha])
        
    for coluna in range(0,colunas):
        
        M2 = 1j*np.sin(-2*np.pi*x*m/colunas) + np.cos(-2*np.pi*x*m/colunas)
        final[:,coluna] = np.linalg.solve(M2,aux[:,coluna])
    tempo_execucao = time.time() - tempo_inicial
    print('IDFT time:', tempo_execucao)
    return final

def filtro_borda_repetida(imagem, kernel):
    tempo_inicial = time.time()
    size = imagem.shape
    M = size[0]-1 # M = 199
    N = size[1]-1 # N = 199
    
    dst = np.zeros((N+1,N+1))

    K = M+2 # K = 201
    imagem2           = np.zeros((K+1, K+1))
    imagem2[1:K,1:K]  = imagem
    imagem2[0,1:K]    = imagem[M,:] # Fronteira de cima
    imagem2[K,1:K]    = imagem[0,:] # Fronteira de baixo
    imagem2[1:K,0]    = imagem[:,N] # Fronteira esquerda
    imagem2[1:K,K]    = imagem[:,0] # Fronteira direita
    imagem2[0,0]      = imagem[M,N] # Ponta superior esquerda
    imagem2[0,K]      = imagem[M,0] # Ponta superior direita
    imagem2[K,0]      = imagem[0,N] # Ponta inferior esquerda
    imagem2[K,K]      = imagem[0,0] # Ponta inferior direita

    # Filtro cru
    for i in range(1,K):
        for j in range(1,K):        
            dst[i-1,j-1]=np.sum(np.sum(np.multiply(imagem2[i-1:i+2,j-1:j+2],kernel)))
    tempo_execucao = time.time() - tempo_inicial
    print('FBR time:', tempo_execucao)
    return dst

def filtro_sem_borda(imagem, kernel):
    size = imagem.shape
    N = size[1]-1
    dst = np.zeros((N+1,N+1))
    tempo_inicial = time.time()
    # Filtro cru
    for i in range(1,N):
        for j in range(1,N):        
            dst[i,j]=np.sum(np.sum(np.multiply(imagem[i-1:i+2,j-1:j+2],kernel)))
            tempo_execucao = time.time() - tempo_inicial
    print('Tempo de execução em segundos:', tempo_execucao)
    return dst

def filtro_conserva_borda(imagem, kernel):
    size = imagem.shape
    N = size[1]-1
    dst = np.zeros((N+1,N+1))
    tempo_inicial = time.time()
    # Filtro cru
    for i in range(1,N):
        for j in range(1,N):        
            dst[i,j]=np.sum(np.sum(np.multiply(imagem[i-1:i+2,j-1:j+2],kernel)))
            tempo_execucao = time.time() - tempo_inicial
    print('Tempo de execução em segundos:', tempo_execucao)
    imagem[1:N,1:N] = dst[1:N,1:N]

    return imagem

def troca0por1(matriz, fourier_imagem):
    linhas, colunas = matriz.shape
    flag = 0
    
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i,j]==0j: 
                print(fourier_imagem[i,j])
                matriz[i,j]=1
                flag = 1
    if flag==0:
        print("No switching was necessary")
    return matriz