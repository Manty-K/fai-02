from kanren import run,Relation,fact,facts,var

connectsTo = Relation('connects to')

def joinlist(l1,l2):
    for i in l2 :
        l1.append(i)
    return l1


factlist = [
    ('Pune',('Mumbai',10)),
      ('Mumbai',('Delhi',50)),
            ('Delhi',('Nagar',50)),

        ('Pune',('Nashik',50)),
        ('Nashik',('Pawar',30)),
           ('Satara',('Delhi',30)),
                ('Aurangabad',('Yawatmal',30)),
    ]




exploredset = []

def traverse(src,xs:list):

    if len(xs) == 0:
        return []

    directList = directs(src,xs)

    dls = []
    for fl in directList:
        dls.append(fl[0])

    tl = tlist(dls,xs)

    return joinlist(dls,tl)

def tlist(ls,xs):
    myli = []

    for l in ls:
        myli = joinlist(traverse(l,remaining(l,xs)),myli)
    return myli

def directs(src,xs):
    d = var();
    for f  in xs:
        fact(connectsTo, f[0],f[1])
    return run(0,d,connectsTo(src,d))

def remaining(src,xs):
    remlist = []
    for i in xs:
        if i[0] == src:
            continue
        remlist.append(i)
    return remlist

    

def road(x,y,ls):
    if(y in traverse(x,ls)):
        return True
    else:
        return False

print(road('Pune','Aurangabad',factlist))

