import time

from bankaccount.domain.operations import addAccount, insertAccount, removeAccount, \
    summing, replaceAccount, maximum
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
    assert(replaceAccount([{"day":22, "value":22, "type":'in', "description":'pizza'}],22,'in','pizza',300)==[{"day":22, "value":300, "type":'in', "description":'pizza'}])
    
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

def testSumming():
    assert(summing([{"day":22, "value":22, "type":'in', "description":'pizza'}, \
                    {"day":13, "value":23, "type":'in', "description":'pizza'}],'in')) == 45
    
def testMaximum():
    assert(maximum([{"day":22, "value":22, "type":'in', "description":'pizza'}, \
                    {"day":22, "value":23, "type":'in', "description":'pasta'}],'in', 22)) == 23
                    
def testFiltering():
    assert(maximum([{"day":22, "value":22, "type":'in', "description":'pizza'}, \
                    {"day":22, "value":23, "type":'out', "description":'pasta'}],'in', 22)) == \
                    [{"day":22, "value":22, "type":'in', "description":'pizza'}]
    assert(maximum([{"day":22, "value":22, "type":'in', "description":'pizza'}, \
                    {"day":22, "value":23, "type":'in', "description":'pasta'}],'in', 23)) == \
                    [{"day":22, "value":22, "type":'in', "description":'pizza'}]
    
    
def testAll():
    testAddAccount()
    testInsertAccount()
    testRemoveAccount()
    testReplaceAccount()
    testSumming()
    testMaximum()