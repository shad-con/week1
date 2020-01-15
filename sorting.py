import numpy as np
import time

arr=np.random.random(100)

def sort(arr):
    t=time.clock()
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if arr[i] < arr[j]:
                moving = arr[i] # save the i-th value which will be delete in the next line
                arr = np.delete(arr, i) # delete i-th value
                arr = np.insert(arr, j, moving) # put the i-th value in front of j-th value
    t=time.clock() - t
    print(str(t))
    return arr