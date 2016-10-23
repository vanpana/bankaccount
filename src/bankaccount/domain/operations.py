import time
from _warnings import filters
import Accounts


def addAccount(accounts,value,ttype,description):
    '''
    Function that adds a new transaction with value, type and description to the accounts
    
    input data:
    accounts - the list of all transactions
    value - an integer
    type - in/out
    description - info about the transaction
    
    output data:
    accounts' - the new list of transactions
    '''
    aux={"day":time.strftime("%d"),"value":value,"type":ttype,"description":description}
    accounts.append(aux)
    return accounts

def insertAccount(accounts,day,value,ttype,description):    
    '''
    Function that inserts a new transaction with day, value, type and description to the accounts
    
    input data:
    day - the day of the transaction
    accounts - the list of all transactions
    value - an integer
    type - in/out
    description - info about the transaction
    
    output data:
    accounts' - the new list of transactions
    '''
    aux={"day":day,"value":value,"type":ttype,"description":description}
    accounts.append(aux)
    return accounts


def removeAccount(accounts,*arg):
    '''
    Function that removes data from the accounts according to the arguments that were given.
    If it's only one argument and is a day, the function deletes all data on that day.
    If it's only one argument and is a type, the functions deletes all data of that type.
    If there are two arguments, the function deletes all data between the days
    
    
    input data:
    accounts - the list of all transactions
    *arg - one day, one type OR two days
    
    output data:
    accounts' - the new list of transactions
    '''
    if len(arg)==1:
        if arg[0]!='out' and arg[0]!='in':
            i=0
            while i<len(accounts):
                if accounts[i]["day"]==arg[0]:
                    accounts[i:]=accounts[i+1:]
                    i=i-1
                i=i+1
            return accounts
        if arg[0]=='out' or arg[0]=='in':
            i=0
            while i<len(accounts):
                if accounts[i]["type"]==arg[0]:
                    accounts[i:]=accounts[i+1:]
                    i=i-1
                i=i+1
            return accounts
    if len(arg)==2:
        if arg[0]!='out' and arg[0]!='in' and arg[1]!='out' and arg[1]!='in':
            i=0
            while i<len(accounts):
                if accounts[i]["day"]>=arg[0] and accounts[i]["day"]<=arg[1]:
                    accounts[i:]=accounts[i+1:]
                    i=i-1
                i=i+1
            return accounts
    return False

def replaceAccount(accounts,day,ttype,description,value): 
    '''
    This function is used to replace the value on a day with a certain description.
    
    input data:
    day - the day of the transaction
    accounts - the list of all transactions
    value - an integer (which will be used for replacement)
    type - in/out
    description - info about the transaction
    
    output data:
    accounts' - the new list of transactions
    '''   
    for i in range(0,len(accounts)):
        if (accounts[i]["day"]==day and accounts[i]["description"]==description):
            accounts[i]["value"]=value
    return accounts

def listAccount(accounts,*arg):
    '''
    Function that returns lists for printing on the screen.
    
    input data:
    accounts - the list of all transactions
    arg - could be in/out OR in/out </=/>
    
    output data:
    returns a list
    '''
    if len(arg)==1:
            return (list(filter(lambda x: x['type']==arg[0],accounts)))
    if len(arg)==2:
        if arg[0]=='<':
            return (list(filter(lambda x: int(x['value'])<int(arg[1]),accounts)))
        if arg[0]=='=':
            return (list(filter(lambda x: int(x['value'])==int(arg[1]),accounts)))
        if arg[0]=='>':
            return (list(filter(lambda x: int(x['value'])>int(arg[1]),accounts)))
        if arg[0]=='balance':
            s=0
            for i in accounts:
                if (int(i['day'])==int(arg[1]) and i['type']=='in'):
                    s+=int(i['value'])
                    
            for i in accounts:
                if (int(i['day'])==int(arg[1]) and i['type']=='out'):
                    s-=int(i['value'])   
            return s
        
def summing(accounts,*arg):
    '''
    Function that returns the sum of a type
    
    input data:
    accounts - the list of all transactions
    arg - type of the transaction
    
    output data:
    s - sum of that type
    '''
    s=0
    for i in accounts:
        if i['type']==arg[0]:
            s+=int(i['value'])
    return s

def maximum(accounts,*arg):
    '''
    Function that gets the maximum value in a day of a type
    
    input data:
    accounts - the list of all transactions
    arg - arguments: type, day
    
    output data:
    m - maximum value
    '''
    m=0
    for i in accounts:
        if i['type']==arg[0] and int(i['day'])==int(arg[1]) and int(i['value'])>int(m):
            m=int(i['value'])
    return m

def filtering(accounts,*arg):
    '''
    Function that filters transactions
    
    input data:
    accounts - the list of all transactions
    arg - arguments: type, type/value
    
    output data:
    accounts' - list of filtered transactions
    '''
    if (len(arg)==1):
        accounts[:]=[i for i in accounts if i['type']==arg[0]]
    if (len(arg)==2):
        accounts[:]=[i for i in accounts if i['type']==arg[0] and int(i['value'])<int(arg[1])]
    return accounts   

def undoOp(accounts,accountsBackup,transactionNo):
    '''
    Function that undoes the last operation.
    input data:
    accounts - the list of all transactions
    accountsBackup - the list of all backups
    transactionNo - number of the current transaction
    
    output data:
    accounts' - the new list of all transactions
    accountsBackup' - the new list of backup list
    transactionNo' - the new transaction number
    
    '''
    accountsBackup.pop()
    transactionNo-=1
    accounts=accountsBackup[transactionNo][:]
    return accounts,accountsBackup,transactionNo