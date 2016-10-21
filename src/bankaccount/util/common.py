'''
Function that checks if the input arguments correspond to the function

input data:
cmd - String
arg - Tuple

output data:
True - if arguments are all right
False - if arguments input is not good
'''

def checkArgs(cmd,arg):
    x=len(arg)
    if cmd=='add':
        if x==3:
            return True
        else:
            return False
    if cmd=='insert':
        if x==4:
            return True
        else:
            return False
    if cmd=='remove':
        if x==1:
            return True
        if x==3 and arg[1]=='to':
            return True
        return False
    if cmd=='replace':
        if x==5:
            return True
        else:
            return False
    if cmd=='list':
        if x==0 or x==1 or x==2:
            return True
        else:
            return False
    if cmd=='sum':
        if x==1:
            return True
        else:
            return False
    if cmd=='max':
        if x==2:
            return True
        else:
            return False
    if cmd=='filter':
        if x==1 or x==2:
            return True
        else:
            return False
    
        
'''
Function that removes arguments that aren't required for functions to run correctly

input data:
cmd - String
arg - Tuple

output data:
arg' - new Tuple with arguments required for functions
'''
def removeUselessArgs(cmd,arg):
    if cmd=='remove':
        if len(arg)==3:
            arg[1:]=arg[2:]
        
    if cmd=='replace':
        arg[3:]=arg[4:]
    return arg

def printAccount(accounts):
    for i in range(0,len(accounts)):
        print(accounts[i]['day'],accounts[i]['value'],accounts[i]['type'],accounts[i]['description'])
        
def backup(accounts,accountsBackup):
    accountsBackup.append(accounts)
    return accountsBackup