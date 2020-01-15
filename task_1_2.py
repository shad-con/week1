from math import sqrt

for x0 in range(1, 9):
    for y0 in range(1, 9):
        for x1 in range(1,9):
            for y1 in range(1,9):
                distance = sqrt((x1-x0)**2+(y1-y0)**2)
                if x1 == x0 and y1 == y0:
                    continue
                print("{},{} to {},{} distance {}".format(x0,y0,x1,y1,distance))
