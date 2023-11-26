
import subprocess
from colorama import Fore

class Position:
    def __init__(self, posx : int, posy: int):
        self.posx = posx
        self.posy = posy
    def __str__(self) -> str:
        return f'{(self.posx,self.posy)}'

class Window:
    def __init__(self, name : str, pos : Position):
        self.name = name
        self.pos = pos
        self.width = 100
        self.height = 100
    def __str__(self) -> str:
        return self.name + ' | ' + f'Position : {self.pos}' + ' | ' + f'Dimension: {(self.width,self.height)}';

    def resize(self,width: int,height:int):
        if(width<=0 | height<=0 ):
            print('Width and height should be more than 0')
        self.width = width
        self.height = height
    def changePos(self,xcor:int,ycor:int):
        self.pos = Position(xcor,ycor)

    def getDimension(self):
        return (self.width,self.height)

dummyWindows1 =  [
    Window('vscode',Position(0,3)),
      Window('chrome',Position(0,0))
]
dummyWindows2 =  [
    Window('postman',Position(-1,30)),
      Window('brave',Position(10,30))
]


class MyProgram:
    
    def __init__(self) -> None:
        # self.windows  = []
        # self.minimizedWindows = []
        # self.activeWindow = False
        self.displayedWindows  = dummyWindows1
        self.minimizedWindows = dummyWindows2
        self.activeWindow = True
 

    def checkExististence(self,name):
        for w in self.displayedWindows:
            if w.name == name :
                return True
        return False
    
    def displayAllWindows(self):
        print(Fore.BLUE+ 'Displayed: '+Fore.RESET)
        self.getAllDisplayedWindows()
        print(Fore.CYAN+ 'Minimized: '+Fore.RESET)
        self.getAllMinimizedWindows()
    def getAllDisplayedWindows(self)-> int:
        for i in range(len(self.displayedWindows)):
            print(f'{i}: {self.displayedWindows[i]} ')
    def getAllMinimizedWindows(self)-> int:
        for i in range(len(self.minimizedWindows)):
            print(f'{i}: {self.minimizedWindows[i]}')



    def createWindow(self):
        name = input('Name of window : ')
        if name.strip() == '':
            print('Name cannot be empty')
            self.createWindow()
        exists = self.checkExististence(name)
        if exists:
            print(f'{name} already exists :)')
            return
        wind = Window(name,pos=Position(0,0))
        self.displayedWindows.insert(0,wind)
        self.changeActiveStatus(True)
        print(f"{Fore.CYAN}{wind.name} {Fore.RESET}created!")

    def destroyActiveWindow(self):
        if not self.activeWindow:
            print('No Window active')
            return;
        if len(self.displayedWindows) == 0:
            print('Not Windows to destroy')
            return;
        wind =  self.displayedWindows[0] 
        del self.displayedWindows[0] 
        self.changeActiveStatus(False)
        print( Fore.CYAN + f'{wind.name}'+ ' ' + Fore.RED+'destroyed'+ Fore.RESET)    

    def destroyMinimisedWindow(self):
        if len(self.minimizedWindows) == 0:
            print('Nothing to destroy')
            return
        
        print('Select window to destroy')
        self.getAllMinimizedWindows()
        option = input()
        optionInt = int(option)

        if int(optionInt) < len(self.minimizedWindows):
            wind = self.minimizedWindows[optionInt]
            del self.minimizedWindows[optionInt]
            print( Fore.CYAN + f'{wind.name}'+ ' ' + Fore.RED+'destroyed'+ Fore.RESET)
    def resizeWindow(self):

        if not self.activeWindow:
            print('No Window active')
            return;
        if len(self.displayedWindows) == 0:
            print('Not Windows to resize')
            return;
        wind =  self.displayedWindows[0]

        print(f'Current dimensions of {wind.name}: {wind.getDimension()}')
        width = int(input('Enter Width: '))
        height = int(input('Enter Height: '))
        wind.resize(width,height)
        del self.displayedWindows[0]
        self.displayedWindows.insert(0,wind)

    def changeWindowPosition(self):
        if not self.activeWindow:
            print('No Window active')
            return;
        if len(self.displayedWindows) == 0:
            print('Not Windows to resize')
            return;
        wind =  self.displayedWindows[0]
        print(f'Current position of {wind.name}: {wind.pos}')
        xcor = int(input('Enter new X value: '))
        ycor = int(input('Enter new Y value: '))
        wind.changePos(xcor,ycor)
        del self.displayedWindows[0]
        self.displayedWindows.insert(0,wind)



    def changeActiveStatus(self,status: bool):
        self.activeWindow = status;

    def selectDisplayedWindow(self):
        if len(self.displayedWindows) == 0:
            print('No Displayed Windows')
            return
        self.getAllDisplayedWindows()
        option = input('Select Window: ')
        optionInt = int(option)
        if optionInt < len(self.displayedWindows):
            wind = self.displayedWindows[optionInt]
            del self.displayedWindows[optionInt]
            self.displayedWindows.insert(0,wind)
            self.changeActiveStatus(True)

    def selectMininizedWindow(self):
        if len(self.minimizedWindows) == 0:
            print('No Minimized Windows')
            return
        
        self.getAllMinimizedWindows()

        option = input('Select Window: ')
        optionInt = int(option)

        if optionInt <  len(self.minimizedWindows):
            wind = self.minimizedWindows[optionInt]
            self.displayedWindows.insert(0,wind)
            del self.minimizedWindows[optionInt]
            self.changeActiveStatus(True)
        
    def activeWindowInfo(self):
        if self.activeWindow:
            return self.displayedWindows[0]
        else:
            return None
    def minimizeWindow(self):
        if self.activeWindow:
            self.changeActiveStatus(False)
            wind = self.displayedWindows[0]
            self.minimizedWindows.insert(0,wind)
            del self.displayedWindows[0]
        else:
            print('No Active Window')


        

def clrMsgDirect():
    subprocess.run('clear',shell=True)
def clrMsg():
    input('Press enter to continue ')
    subprocess.run('clear',shell=True)

prog = MyProgram()

running = True;

def activeWindowString():
    if prog.activeWindow :
       return prog.displayedWindows[0]
    else:
        return None

while(running):
    print('-------------')
    print(Fore.GREEN+  f'Active Window' +Fore.RESET+ ' : '+Fore.CYAN +f'{activeWindowString()}'+ Fore.RESET)
    print('''
1. Create new window
2. Destroy active window
3. Resize active window
4. Change active window position
5. Minimize active window
6. Display all existing windows
7. Select displayed window   
8. Select minimized window 
9. Destroy minimized window              
10. Exit
          ''')
    print('-------------')

    option = int(input())

    if(option == 1):
        prog.createWindow()
        clrMsg()
    elif (option == 2):
        prog.destroyActiveWindow()
        clrMsg()
    elif (option == 3):
        prog.resizeWindow()
        clrMsg()
    elif (option == 4):
        prog.changeWindowPosition()
        clrMsg()
    elif (option == 5):
        prog.minimizeWindow()
        clrMsg()
    elif (option == 6):
        prog.displayAllWindows()
        clrMsg()
    elif (option == 7):
        prog.selectDisplayedWindow()
        clrMsg()    
    elif (option == 8):
        prog.selectMininizedWindow()
        clrMsg()
    elif (option == 9):
        prog.destroyMinimisedWindow()
        clrMsg()
    elif (option == 10):
        running = False;
    else:
        print('Invalid Input')


