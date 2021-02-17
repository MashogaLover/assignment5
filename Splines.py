import numpy as np
import matplotlib.pyplot as plot
n = 21
h = 0.5
x_i = np.linspace(0.5,10.5,n)
y_i = [1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25]

A = np.zeros(shape=(n-2,n-2)) #First and last sigma are 0 so we dont evaluate those rows
A[0][0] = 4 #Add first and last row since special
A[0][1] = 1
A[n-3][n-4] = 1
A[n-3][n-3] = 4
for i in range(1,n-3): #Add all other rows, -3 so we get same dimentions as b
    A[i][i-1] = 1
    A[i][i] = 4
    A[i][i+1] = 1
print("Matrix A: %s" % A)

b = []
for i in range(1,n-1): #Natural splines so sigma_0 and sigma_n is 0
    b.append(y_i[i-1] - 2*y_i[i] + y_i[i+1])
print("b array: %s" % b)

sigma_i = [0] #Add sigma_0 and sigma_n that we took away while solving the rest
sigma_i = np.concatenate((sigma_i, np.linalg.solve(A,b)))
sigma_i = np.concatenate((sigma_i, [0]))
print("sigma array: %s" % sigma_i)

a_i = []
for i in range(1, n):
    a_i.append((sigma_i[i] - sigma_i[i-1])/6*h)
print("a_i: %s" % a_i)
b_i = []
for i in range(1, n):
    b_i.append(sigma_i[i-1]/2)
print("b_i: %s" % b_i)
c_i = []
for i in range(1, n):
    c_i.append(  ((-h*(2*sigma_i[i-1] + sigma_i[i]))/6) + ((y_i[i] - y_i[i-1])/h) )
print("c_i: %s" % c_i)
d_i = []
for i in range(1, n):
    d_i.append(y_i[i-1])
print("d_i: %s" % d_i)

for i in range(0,n-1):
    x = np.linspace(i, i+h)
    y = (a_i[i]*(x - x_i[i]))**3 + (b_i[i]*(x - x_i[i]))**2 + (c_i[i]*(x - x_i[i])) + d_i[i]
    plot.plot(x,y)
plot.show()
