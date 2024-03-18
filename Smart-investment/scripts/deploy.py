from brownie import Invest,accounts,network


def deploy_bet():
    
    recipient_address = accounts[1]
    deployed_contract = Invest.deploy(recipient_address, {'from': accounts[0]})

    # Print contract address
    print("Contract deployed at:", deployed_contract.address)


def main():
    deploy_bet()
    