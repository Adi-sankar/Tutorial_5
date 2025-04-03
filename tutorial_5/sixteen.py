import numpy as np

a = np.random.randint(0, 21, (3, 3))
b = np.random.randint(0, 21, (3, 3))

sum_matrix = a + b
product_matrix = np.dot(a, b)
transpose = product_matrix.T

print("Matrix a:")
print(a)

print("Matrix b:")
print(b)

print("Matrix Addition (Sum):")
print(sum_matrix)

print("Matrix Multiplication (Product):")
print(product_matrix)

print("Transpose of the Product Matrix:")
print(transpose)
