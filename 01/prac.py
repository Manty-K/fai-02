from kanren import permuteq,run,var,seteq,membero,lall,facts,Relation,conde,lany,eq,fact


windowState = Relation()

windowPosition = Relation()

windowDimension = Relation()

order = ['spotify','chrome',]

stateFactList =  [
    ('spotify','disp'),
    ('chrome','disp'),
    ('vscode','mini'),
    ('notes','ne'),
    ]

for f in stateFactList:
    fact(windowState,f[0],f[1])



facts(windowPosition,
      ('spotify',(0,0)),
         ('chrome',(20,10)),
       ('vscode',(2,1)),
      )
facts(windowDimension,
      ('spotify',(100,100)),
              ('chrome',(200,150)),
       ('vscode',(200,300)),    
      )

## Returns all windows Existing windows (displayed, minimized)
def allExistingWindows():
    x = var()
    return run(0,x, lany(windowState(x,'disp'),windowState(x,'mini')))

def createWindow():
    name = input('Name of window: ')
    if name.strip()=='':
        print('Name should not be empty')
    fact(windowState, name,'disp')
    print('facts created')


running = True
while(running):
    print('1. Create')
    print('2. Display')
    print('10. Exit')
    option = input('Choose option: ')
    try:
        optionint = int(option)
        if optionint == 1:
            createWindow()
        elif optionint == 2:
            print(allExistingWindows())
        elif optionint == 10:
            running = False

        
    except:
        print('Error')


def optionSelector(x):

    if x == 1:
        createWindow()
    elif x == 2:
        allExistingWindows()
    elif x == 10:
        running = False