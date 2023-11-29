from kanren import run,facts,Relation,fact,var

path = [
    ('A','B',20),
       ('A','K',30),
     ('B','C',40),
      ('C','D',90),
             ('K','C',50),
        #  ('D','A',90),

]
def join(l1:list,l2:list):
    for e in l2:
        l1.append(e)
    return l1


def directs(x,ls):
    y = var()
    connectTo = Relation()
    for f in ls:
        fact(connectTo,f[0],(f[1],f[2]))
    result = run(0,y,connectTo(x[0],y))
    newRes = []
    for r in result:
        newRes.append((r[0],r[1]+x[1]))
    return newRes

def remaininig(x,ls):
    newRemaining = []
    for t in ls:
        if t[0] == x[0]:
            pass
        elif t[1] == x[0]:
            continue
        else: 
            newRemaining.append(t)
    return newRemaining

def map(ds:list,xs:list):
    myli = []
    for d in ds:
        myli = join(traverse(d,xs),[])
    return myli

def traverse(x,ls:list):
    if len(ls) == 0:
        return []
    dire = directs(x,ls)
    directList = []
    for d in dire:
        directList.append(d)

    return join(directList,map(directList,remaininig(x,ls)))


def distance(src,dst,ls):
    x = var()
    dist = Relation('distance')

    for tv in traverse((src,0),ls):
        fact(dist, tv[0],tv[1])

    value = run(0,x,dist(dst,x))

    return value;


def road(src,dst,ls):

    if len(distance(src,dst,ls)) > 0:
        return True
    return False;

print(distance('A','C',path))
# print(road('A','K',path))