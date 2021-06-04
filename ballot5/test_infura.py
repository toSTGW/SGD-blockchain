import json
from web3 import Web3
from constants import const
# web3 = Web3(Web3.WebsocketProvider("https://ropsten.infura.io/v3/747b0843f2e04ab7a384fa175deba232"))
web3 = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/ws/v3/747b0843f2e04ab7a384fa175deba232"))

# web3.eth.defaultAccount = "0x3648109582d7DA09D098faB0c8Aaa3543f633E2f"

abi = json.loads(const.ABI)
address = web3.toChecksumAddress(const.CONTRACT_ADDRESS)

# bytecode = const.BYTECODE
Ballot4 = web3.eth.contract(abi=abi,bytecode=bytecode)
transaction = Ballot4.constructor().buildTransaction()
transaction.update({ 'gas' : 2000000 })
transaction.update({ 'nonce' : web3.eth.getTransactionCount('0x3648109582d7DA09D098faB0c8Aaa3543f633E2f') })
private_key = "D522CE6DE0C170EEAB10517605E58FD3789F6784744DA7DBE68818C30145A795"
signed_tx = web3.eth.account.signTransaction(transaction, private_key)
txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)

# abi = json.loads(const.ABI)
Ballot4 = web3.eth.contract(address=address, abi=abi)

web3.eth.defaultAccount = "0x3648109582d7DA09D098faB0c8Aaa3543f633E2f"
transaction = Ballot4.functions.getAllIntercept().buildTransaction()
transaction.update({ 'gas' : 2000000 })
transaction.update({ 'nonce' : web3.eth.getTransactionCount('0x3648109582d7DA09D098faB0c8Aaa3543f633E2f') })
private_key = "D522CE6DE0C170EEAB10517605E58FD3789F6784744DA7DBE68818C30145A795"
signed_tx = web3.eth.account.signTransaction(transaction, private_key)
txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)














