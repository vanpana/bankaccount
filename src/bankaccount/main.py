#{"day":day,"value":value,"type":type,"description":description
#day=0-30
#value=int
#type=in/out
#description=String
from bankaccount.ui.console import getCommand, readCommands, uiMenu


if __name__ == '__main__':
    #testAll()
    #bankaccount.test_main()
    mode=0
    while mode!=1 and mode!=2:
        mode=input("Hello! Choose how you would like to input commands: 1 - menu based, 2 - console based: ")
        if mode!=1 and mode!=2:
            print("Invalid input! Try again!")
    if mode==1:
        uiMenu()
    if mode==2:
        print("Hello! Input your commands:")
        cmd,arg=getCommand()
        readCommands(cmd,arg)