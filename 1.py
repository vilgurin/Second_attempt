def lines_intersection(k1, c1, k2, c2):
    if k1 != k2:
        spot = {}
        x = (c2-c1)/(k1-k2)
        y = k1*x +c1
        spot = x,y
        return spot[0],spot[1]
print(lines_intersection(3,-4,2,-1))
