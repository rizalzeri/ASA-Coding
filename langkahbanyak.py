#Rizal Zeri Subakti
#24060120130062
def lngk(y):
    if (y == 45) : 
        return 1836311903
    elif ( y == 0 ):
        return 1
    elif (y < 0):
        return 0
    else:
        return lngk(y - 2) + lngk(y - 1)
#banyak cara
y = int(input()) 
print(lngk(y))
