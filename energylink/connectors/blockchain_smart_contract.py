
from web3 import Web3

def deploy_smart_contract(web3_provider, contract_code, deployer_address, private_key):
    """Deploy a blockchain smart contract."""
    web3 = Web3(Web3.HTTPProvider(web3_provider))
    compiled_contract = web3.eth.contract(abi=contract_code['abi'], bytecode=contract_code['bytecode'])
    transaction = compiled_contract.constructor().buildTransaction({
        'from': deployer_address,
        'nonce': web3.eth.getTransactionCount(deployer_address),
        'gas': 6721975,
        'gasPrice': web3.toWei('20', 'gwei')
    })
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash)
            