import numpy as np

def check_formula(matrix, eigennumber, eigenvector):
    a = eigennumber * eigenvector
    b = np.dot(matrix, eigenvector)
    if np.allclose(a, b):
        print('Рівність виконується')
    else:
        print("Рівність не виконується")

def eigennumbers_and_eigenvectors(arr):
    eigenvalues, eigenvectors = np.linalg.eig(np.array(arr))
    return eigenvalues, eigenvectors

a = np.array([[1,2,0],[0.5,2,5],[3,2,1]])
b, c = eigennumbers_and_eigenvectors(a)
print(b)

k = check_formula(a, b, c)

