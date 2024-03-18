from brownie import Invest,accounts,network

def transfer():
    trans=Invest[-1]

    trans.collectAndTransfer({"from":accounts[0],"value":100000000000000000})


def check_balance():
    trans=Invest[-1]

    balance=trans.getBalance(accounts[0],{"from":accounts[0]})
    print("Balance:", balance)


def main():
    transfer()
    