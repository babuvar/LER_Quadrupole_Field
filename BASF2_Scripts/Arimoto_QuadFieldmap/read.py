import  numpy as np

data = np.loadtxt( 'quad.dat',  dtype = np.double )
data2 = data[(data[:,1] >= 0) & (data[:,1] <= 180)] 

#print(data2)

np.savetxt('quad2.dat', data2, fmt='%12f')
