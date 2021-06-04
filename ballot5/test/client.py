import json
from web3 import Web3


web3 = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/ws/v3/747b0843f2e04ab7a384fa175deba232"))
web3.eth.defaultAccount = "0x5F092a084e5CB8C65b4Cf52DA88d230B5DfE9F62"

address = web3.toChecksumAddress("0x93D41E9F805557F3cbb67f382950470f2887Ead2")
abi = json.loads('[{"constant":false,"inputs":[],"name":"calltest1","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"clear","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"concatInterceptAndCoef","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"n","type":"uint256"}],"name":"fillParameters","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"all_intercepts","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"all_coefs","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"n","type":"uint256"}],"name":"testConcat","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[],"name":"test1","type":"event"}]')

testRopsten = web3.eth.contract(address=address, abi=abi)

transaction = testRopsten.functions.fillParameters(0).buildTransaction()
transaction.update({'gas': 8000000})
transaction.update({'nonce': web3.eth.getTransactionCount("0x5F092a084e5CB8C65b4Cf52DA88d230B5DfE9F62")})
signed_tx = web3.eth.account.signTransaction(transaction, "20F7949473CEBC05BBAD4590FF00569B1C1DD4D9451E14C781BF08ADD831C85F")
txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
print(txn_receipt)

concattransaction = testRopsten.functions.concatInterceptAndCoef().buildTransaction()
concattransaction.update({'gas': 8000000})
concattransaction.update({'nonce': web3.eth.getTransactionCount("0x5F092a084e5CB8C65b4Cf52DA88d230B5DfE9F62") + 1})
signed_tx = web3.eth.account.signTransaction(concattransaction, "20F7949473CEBC05BBAD4590FF00569B1C1DD4D9451E14C781BF08ADD831C85F")
txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
print(txn_receipt)


cleartransaction = testRopsten.functions.clear().buildTransaction()
cleartransaction.update({'gas': 8000000})
cleartransaction.update({'nonce': web3.eth.getTransactionCount("0x5F092a084e5CB8C65b4Cf52DA88d230B5DfE9F62") + 1})
signed_tx = web3.eth.account.signTransaction(cleartransaction, "20F7949473CEBC05BBAD4590FF00569B1C1DD4D9451E14C781BF08ADD831C85F")
txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
print(txn_receipt)

all_intercepts = testRopsten.functions.all_intercepts().call()
all_coefs = testRopsten.functions.all_coefs().call()
print(all_intercepts)
print(all_coefs)





















