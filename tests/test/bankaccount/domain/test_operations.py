import time
from bankaccount.domain.operations import addAccount, insertAccount, removeAccount
from bankaccount.util.common import backup


def testAddAccount():
    assert(addAccount([],100,'out','desc')==[{"day":time.strftime("%d"),"value":100,"type":'out',"description":'desc'}])    

def testInsertAccount():
    assert(insertAccount([],21,100,'out','desc')==[{"day":21,"value":100,"type":'out',"description":'desc'}])

def testRemoveAccount():
    assert(removeAccount([{"day":22, "value":22, "type":'in', "description":'pizza'}],22)==[])
    assert(removeAccount([{"day":22, "value":22, "type":'in', "description":'pizza'}],'in')==[])
    assert(removeAccount([{"day":22, "value":22, "type":'in', "description":'pizza'}, {"day":23, "value":22, "type":'in', "description":'pizza'}],22,23)==[])

def testReplaceAccount():
    pass

def testAll():
    testAddAccount()
    testInsertAccount()
    testRemoveAccount()
    testReplaceAccount()
    
def addSomeValuesForTesting(accounts,accountsBackup):
    addAccount(accounts, '20', 'out', 'pizza')
    accountsBackup = accountsBackup + [accounts[:]]
    addAccount(accounts, '30', 'out', 'pasta')
    accountsBackup = accountsBackup + [accounts[:]]
    addAccount(accounts, '50', 'out', 'rice')
    accountsBackup = accountsBackup + [accounts[:]]
    addAccount(accounts, '1000', 'in', 'salary')
    accountsBackup = accountsBackup + [accounts[:]]
    addAccount(accounts, '20', 'out', 'potatoes')
    accountsBackup = accountsBackup + [accounts[:]]
    addAccount(accounts, '100', 'in', 'ads')
    accountsBackup = accountsBackup + [accounts[:]]
    addAccount(accounts, '30', 'out', 'mobile')
    accountsBackup = accountsBackup + [accounts[:]]
    addAccount(accounts, '10', 'out', 'coffee')
    accountsBackup = accountsBackup + [accounts[:]]
    addAccount(accounts, '20', 'out', 'milk')
    accountsBackup = accountsBackup + [accounts[:]]
    addAccount(accounts, '800', 'in', 'bank')
    accountsBackup = accountsBackup + [accounts[:]]
    return accounts,accountsBackup