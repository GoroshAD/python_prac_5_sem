def genf() :
    print("qq")
    res = yield "start"
    while res :
        res = yield f"/{res}/"

def walk2d() :
    coord = 0, 0
    while delta := (yield coord) :
        coord = coord[0] + delta[0], coord[1] + delta[1]


ite = genf()
#ite.send(123) - error
ite.send(None) #~ next(ite)

send = None
ite = walk2d()
ite.send(send)
while (send := eval(input())) :
    print(ite.send(send))
    
