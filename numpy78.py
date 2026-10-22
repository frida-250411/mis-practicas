import numpy as np
#DEFINICION DE UNA MATRIZ
A= np.array([[1,2],[3,4]])
B= np.array([[5,6],[7,8]])
#SUMA DE ELEMENTO A ELEMENTO
suma= A+B
print("..SUMA(A+B)..")
print(suma)
#MULTIPLICACION
prod_elem=A*B
print("..MULTIPLICACION(A*B)..")
print(prod_elem)
#producto de matrices
prod_mat=np.dot(A,B)
print("..PRODUCTO DE MATRICES(A*B)..")
print(prod_mat) 
#TRANSPUESTA
transpuesta= A.T
print("..TRANSPUESTA DE A.T ..")
print(transpuesta)
#DETERMINANTE E INVERSA
det=np.linalg.det(A)
inv=np.linalg.inv(B)
print("..DETERMINANTE DE A..")
print(det)
print("..DETERMINANTE DE B..")
print(inv)

