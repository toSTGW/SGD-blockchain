import json
from web3 import Web3
from constants import const

# web3 = Web3(Web3.HTTPProvider(const.GANACHE_URL))
web3 = Web3(Web3.WebsocketProvider(const.GANACHE_URL))
print(const.GANACHE_URL)
Ballot5 = web3.eth.contract(abi=const.ABI, bytecode=const.BYTECODE)
transaction = Ballot5.constructor().buildTransaction()
transaction.update({ 'gas' : 8000000 })
transaction.update({ 'nonce' : web3.eth.getTransactionCount('0x71865cae76EAEd3fC56Eb7e901850819F3c59aaC')+1 })
private_key = "04f441475c9bb113380ebbb34d3ed1455bef6487d07de54109cffe4a722743e6"
signed_tx = web3.eth.account.signTransaction(transaction, private_key)
txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)

print(txn_receipt)
print("合约部署成功，合约地址为："+txn_receipt.contractAddress)

