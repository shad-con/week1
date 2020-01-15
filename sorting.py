import numpy as np
import time

arr=np.random.random(100)

def sort(arr):
    t=time.clock()
    for i in range(0,100):
        for j in range(0,100):
            if arr[i] < arr[j]:
                moving = arr[i]
                arr = np.delete(arr, i)
                arr = np.insert(arr, j, moving)
    t=time.clock() - t
    print(str(t))
    return arr