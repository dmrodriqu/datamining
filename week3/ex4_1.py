# principles of data mining example 4.1

import numpy as np

def FS(mat):
    return float(sum([x for x in mat if x[0] == x[1]])[0])

def stats(mat):
    f = sum(mat[:,0])
    s = sum(mat[:,1])
    print float(FS(mat)/f)

i = 0
while i < 10:
    a = np.random.randint(2, size=(100000, 2))
    stats(a)
    i +=1





