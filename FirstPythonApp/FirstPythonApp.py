import numpy as np
x = np.array([1,2,3,4,])

y = np.mean(x)

print('Hello world '+ str(x[1]))
print( 'this is the ' + 'mean ' + str(y))

val = int(input("enter the value:"))
x_new = np.append(x, val)

print(x_new)
y_new = np.mean(x_new)
print( 'this is the new ' + 'mean ' + str(y_new))