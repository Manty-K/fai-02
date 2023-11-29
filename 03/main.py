from kanren import run, var, Relation,fact,eq

gameboard = [
    (0,0,1),
    (0,1,0),
    (0,2,1),
    (1,0,0),
    (1,1,0),
    (1,2,1),
     (2,0,1),
    (2,1,1),
    (2,2,0),
    ]


def makeMove(x,gs)-> bool:
    if not validMove(gs):
        print('Game board valid nahi hai')
        return False
    if g[2] != 0 or g[2] != 1:
        print('Areee 0 nahi toh 1 use harna hai..')
        return False
    if x[0] >=3:
        print('row 3 ke upar tere baap ne diya value')
        return False
    if x[1] >=3:
        print('column 3 ke upar tere baap ne diya value')
        return False   
    for g in gs:
        if g[0] == x[0] and g[1] == x[1]:
            print('Already us jagah pe dusri value hai')
            return False

    gs.append(x)
    print('Hogay bhai move 👍🏻')
    return True


## Game Draw
def gameDraw(gs): 
    if len(gs) == 9 and (not gameWon(gs)):
        return True
    return False

## Game Won
def gameWon(gs) -> bool:
    versicalwin = verticalSatisfied(gs)
    horizontalwin = hosizontalSatisfied(gs)
    diag1win = diag1Satisfied(gs)
    diag2win = diag2Satisfied(gs)

    if versicalwin or horizontalwin or diag1win or diag2win:
        return True
    else:
        return False




def verticalSatisfied(gs)-> bool:
    mylist = []
    x = var()
    y = var()
    z = var()
    isvalue = Relation()
    for g in gs:
        fact(isvalue,g[0],g[1],g[2])

    for colm in range(3):     
        for valm in range(2):
         output = run(0,(x,y,z),isvalue(x,colm,valm))
         mylist.append(output)

    for v in mylist:
        if len(v) == 3:
            return True
    return False



def hosizontalSatisfied(gs)-> bool:
    mylist = []
    x = var()
    y = var()
    z = var()
    isvalue = Relation()
    for g in gs:
        fact(isvalue,g[0],g[1],g[2])

    for rowm in range(3):     
        for valm in range(2):
         output = run(0,(x,y,z),isvalue(rowm,y,valm))
         mylist.append(output)

    for v in mylist:
        if len(v) == 3:
            return True
    return False


def diag1Satisfied(gs)-> bool:
    mylist = []
    x = var()
    y = var()
    z = var()
    isvalue = Relation()
    for g in gs:
       fact(isvalue,g[0],g[1],g[2])

    for v in range(2):
         output = run(0,(x,y,z),isvalue(x,y,v),eq(x,y))
         mylist.append(output)

    for v in mylist:
        if len(v) == 3:
            return True
    return False

def diag2Satisfied(gs)-> bool:
    mylist = []

    for i in range(2):
        tplist = []
        for g in gs:
            if(g[0] + g[1] == 2) and i == g[2]:
                tplist.append(g)
        mylist.append(tplist)    

    for ml in mylist:
        if len(ml) == 3:
            return True      
    return False


def validMove(gs)->bool:

    totalOnse = 0
    totalZeros = 0

    for g in gs:
        if g[2] == 1:
            totalOnse = totalOnse + 1
        elif g[2] == 0:
            totalZeros = totalZeros + 1
    
    if abs(totalOnse - totalZeros)  <= 1:
        return True
    
    return False

