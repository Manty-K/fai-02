
from kanren import Relation, run, var, fact
import copy

def dire(data ,pth):
    connectedTo = Relation()
    src = data[0]
    ls = data[1]
    y= var()
    z = var()

    for p in pth:
        fact(connectedTo , p[0],p[1],p[2])

    result = run(0,y,connectedTo(src,y,z))
    dirValues = []
    for r in result:
        ls.append(r)
        temp = copy.deepcopy(ls)
        del ls[len(ls)-1]
        dirValues.append((r,temp))

    return dirValues

def remaining(x,ls):
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


def join(l1:list,l2:list):
    for e in l2:
        l1.append(e)
    return l1

def traverse(data,pth):
    if len(pth) == 0:
        return []
    direc = dire(data,pth)
    directList = []
    for d in direc:
        directList.append(d)

    return join(directList,map(directList,remaining(data,pth)))


def go(x,y,ls):
    allp = []
    for t in traverse((x,[x]),ls):
        if y in t:
            allp.append(t[1])
    return allp


# print(go('A','D',path))