import numpy as np

A = np. array([
    [1,-1,2],
    [3,2,2],
    [4,1,2],
    [7,5,6]
    ])
    
print(A)
print("")

# zeros는 () 괄호를 한 번 사용해야함
C = np.random.rand(3,5)
print(C)
print("")

# zeros는 () 괄호를 한 번더 사용해야함
D = np.zeros((2,4))
print(D)
print("")

print(A[0][0])
