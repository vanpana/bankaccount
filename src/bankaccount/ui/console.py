import cmd
from time import sleep

from bankaccount.domain.operations import listAccount, addAccount, insertAccount, removeAccount, \
    replaceAccount, summing, maximum, filtering, undoOp
from bankaccount.util.common import removeUselessArgs, printAccount, checkArgs
from test.bankaccount.domain.test_operations import addSomeValuesForTesting
from matplotlib.testing.jpl_units import day


def uiAddAccount(account,value,ttype,description):
    '''
    Function that checks if the given input data can be used in the function and tells the user if there is any error
    
    input data:
    accounts - the list of all transactions
    value - an integer
    type - in/out
    description - info about the transaction
    
    output data:
    accounts' - the new list of transactions
    '''    
    try:
        aux=int(value)
    except ValueError:
        print ("<value> has to be an integer")
        return False
    
    if ttype!='out' and ttype!='in':
        print ("<type> has to be 'out' or 'in'!")
        return False
    
    addAccount(account,value,ttype,description)
  
def uiInsertAccount(account,day,value,ttype,description):
    '''
    Function that checks if the given input data can be used in the function and tells the user if there is any error
    
    input data:
    day - the day of the transaction
    accounts - the list of all transactions
    value - an integer
    type - in/out
    description - info about the transaction
    
    output data:
    accounts' - the new list of transactions
    '''  
    if int(day)<0 or int(day)>31:
        print("<day> has to be an integer between 0 and 30")
        return False
    try:
        aux=int(value)
    except ValueError:
        print ("<value> has to be an integer")
        return False
    
    if ttype!='out' and ttype!='in':
        print ("<type> has to be 'out' or 'in'!")
        return False
    
    insertAccount(account,day,value,ttype,description)
         
def uiRemoveAccount(account, *arg):
    '''    
    Function that checks if the given input data can be used in the function and tells the user if there is any error
    
    input data:
    accounts - the list of all transactions
    *arg - one day, one type OR two days
    
    output data:
    accounts' - the new list of transactions
    '''   
    try:
        a=int(arg[0])
        OK=1
    except ValueError:
        OK=0

    if len(arg)==1:
        if arg[0]<0 and arg[0]>30:
                print("<day> has to be an integer between 0 and 30")
                return False
        else:
            if OK==0 and arg[0]!='out' and arg[0]!='in':
                print ("<type> has to be 'out' or 'in'!")
                return False
            
    if len(arg)==2:
        if int(arg[0])>int(arg[1]):
            print ("<end day> has to be greater than <start day>")
            return False
    
    removeAccount(account, *arg)
    
def uiReplaceAccount(account,day,ttype,description,value):
    '''
    Function that checks if the given input data can be used in the function and tells the user if there is any error
    
    input data:
    day - the day of the transaction
    accounts - the list of all transactions
    value - an integer (which will be used for replacement)
    type - in/out
    description - info about the transaction
    
    output data:
    accounts' - the new list of transactions
    '''
    if day<0 and day>30:
        print("<day> has to be an integer between 0 and 30")
        return False
    try:
        aux=int(value)
    except ValueError:
        print ("<value> has to be an integer")
        return False
    
    if ttype!='out' and ttype!='in':
        print ("<type> has to be 'out' or 'in'!")
        return False
    
    OK1=False
    OK2=False
    for i in range(0,len(account)):
        if account[i]["type"]==ttype:
            OK1=True
        if account[i]["day"]==day:
            OK2=True    
    if OK1==False or OK2==False:
        print("Inexistent data on input day")
        return False

    replaceAccount(account, day, ttype, description, value)
    
def uiListAccount(accounts,*arg):
    '''
    Function that checks if the given input data can be used in the function and tells the user if there is any error
    
    input data:
    accounts - the list of all transactions
    arg - could be in/out OR in/out </=/>
    
    output data:
    prints data according to the input
    '''
    if len(arg)==1:
        if arg[0]!='out' and arg[0]!='in':
            print ("<type> has to be 'in' or 'out'!")
            return False
    if len(arg)==2:
        if arg[0]!='<' and arg[0]!='=' and arg[0]!='>' and arg[0]!='balance':
            print ("Operator has to be '<' or '=' or '>' or 'balance'!")
            return False
    if (arg==()):
        printAccount(accounts)
        return True
    
    aux=listAccount(accounts,*arg)
    if (arg[0]=='balance'):
        print(aux)
        return True
        
    for i in aux:
        print("({0}, {1}, {2}, {3})".format(i["day"],i["value"],i["type"],i["description"]))

def uiSumming(accounts,*arg):
    '''
    Function that checks if the given input data can be used in the function and tells the user if there is any error
    
    input data:
    accounts - the list of all transactions
    arg - could be in/out OR in/out </=/>
    
    output data:
    prints sum of the input type
    '''
    if arg[0]!='out' and arg[0]!='in':
        print ("<type> has to be 'in' or 'out'!")
        return False
    print (summing(accounts,*arg))

def uiMaximum(accounts,*arg):
    '''
    Function that checks if the given input data can be used in the function and tells the user if there is any error
    
    input data:
    accounts - the list of all transactions
    arg - could be in/out and a day
    
    output data:
    prints max of the input type and day
    '''
    if arg[0]!='out' and arg[0]!='in':
        print ("<type> has to be 'in' or 'out'!")
    try:
        m=int(arg[1])
    except ValueError:
        print ("<day> has to be an integer")
    print(maximum(accounts,*arg))
    
def uiFiltering(accounts,*arg):
    '''
    Function that checks if the given input data can be used in the function and tells the user if there is any error
    
    input data:
    accounts - the list of all transactions
    arg - could be in/out and a day
    
    output data:
    keeps in list only the filtered data
    '''
    if arg[0]!='out' and arg[0]!='in':
        print ("<type> has to be 'in' or 'out'!")
    if len(arg)>1:
        try:
            m=int(arg[1])
        except ValueError:
            print ("<value> has to be an integer")
    filtering(accounts,*arg)

def uiUndoOp(accounts,accountsBackup,transactionNo):
    '''
    Function that checks if the given input data can be used in the function and tells the user if there is any error
    
    input data:
    accounts - the list of all transactions
    accountsBackup - the list of all the backed-up transactions
    transactionNo - integer, number of transactions
    
    output data:
    accounts' - the list before last modification
    '''
    if transactionNo==0:
        print("Can't undo, no previous transaction!")
        return False
    return undoOp(accounts,accountsBackup,transactionNo)

def getCommand():
    '''
    Function that gets the user input and splits it into command and argument(s).
    input:
    user data
    
    output:
    cmd - the command / String
    arg - the argument(s) / Tuple
    '''
    command=raw_input("")
    position=command.find(" ")
    if (position==-1):
        return command,""
    else: 
        cmd=command[:position]
        arg=command[position+1:]
        arg=arg.split(" ")
        return cmd,arg
          
def readCommands(cmd,arg):
    '''
    Checks if inputed commands exists and execute a specific function. It stays in the loop until 'exit' is input.
    
    input data:
    cmd - String
    arg - Tuple
    
    output data:
    according to commands
    '''    
    commands={"add":uiAddAccount,"insert":uiInsertAccount,"remove":uiRemoveAccount,"replace":uiReplaceAccount, "list":uiListAccount, "sum":uiSumming, "max":uiMaximum, "filter":uiFiltering}
    accounts=[]
    accountsBackup=[]
    transactionNo=9
    accounts, accountsBackup = addSomeValuesForTesting(accounts,accountsBackup)
    while True:
        if cmd=='exit':
            break
        if cmd=='undo':
            accounts,accountsBackup,transactionNo = uiUndoOp(accounts,accountsBackup,transactionNo)
        elif cmd in commands:
            if checkArgs(cmd, arg)==True:
                removeUselessArgs(cmd, arg)
                commands[cmd](accounts,*arg)
                if cmd!='list' and cmd!='sum' and cmd!='max':
                    accountsBackup = accountsBackup + [accounts[:]]
                    transactionNo+=1
                print("Command processed!")
            else:
                print("Try inputing the arguments correctly")
        else:
            print("Command not known")
        (cmd,arg)=getCommand()
    printAccount(accounts)

#######MENUBASED

def uiMenu():
    commands={"add":menuAddAccount,"insert":menuInsertAccount,"remove":menuRemoveAccount,"replace":uiReplaceAccount, "list":uiListAccount, "sum":uiSumming, "max":uiMaximum, "filter":uiFiltering}
    accounts=[]
    accountsBackup=[]
    transactionNo=9
    accounts, accountsBackup = addSomeValuesForTesting(accounts,accountsBackup)
    while True:
        print("You can:")
        print("ADD - add a value on current day")
        print("INSERT - add a value on a certain day")
        print("REMOVE - remove data from list")
        print("REPLACE - replace a value on certain day having a input description")
        print("LIST - print values")
        print("SUM - print the sum of transactions of a type")
        print("MAX - get the max of a type on a day")
        print("FILTER - filter types of transactions")
        print("UNDO - undo last modification to the list of transactions")
        print("EXIT - exits the application")
        cmd=raw_input("Input your command in lower-case: ")
        cmd=cmd.strip(" ")
        cmd=cmd.lower()
        if cmd=='exit':
            break
        if commands[cmd](accounts)!=False:
            sleep(2)
            print("Command processed!")

def menuAddAccount(accounts):
    value=raw_input("Input <value>: ")
    ttype=raw_input("Input <type>: ")
    description=raw_input("Input <description>: ")
    uiAddAccount(accounts,value,ttype,description)

def menuInsertAccount(accounts):
    day=raw_input("Input <day>: ")
    value=raw_input("Input <value>: ")
    ttype=raw_input("Input <type>: ")
    description=raw_input("Input <description>: ")
    uiInsertAccount(accounts,day,value,ttype,description)

def menuRemoveAccount(accounts):
    mode=0
    while mode!=1 or mode!=2 or mode!=3:
        mode=raw_input("1: remove day, 2: remove start day to end day, 3: remove type")
        if mode!=1 or mode!=2 or mode!=3:
            print("Invalid input, try again!")
    if mode==1:
        day=raw_input("Input <day>: ")
        uiRemoveAccount(accounts,day)
    if mode==2:
        start_day=raw_input("Input <start day>: ")
        end_day=raw_input("Input <end day>: ")
        uiRemoveAccount(accounts,start_day,end_day)
    if mode==3:
        ttype=raw_input("Input <type>: ")
        uiRemoveAccount(accounts,ttype)