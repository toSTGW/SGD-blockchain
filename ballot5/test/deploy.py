import json
from web3 import Web3

web3 = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/ws/v3/747b0843f2e04ab7a384fa175deba232"))
web3.eth.defaultAccount = "0x3648109582d7DA09D098faB0c8Aaa3543f633E2f"

abi = json.loads('[{"constant":true,"inputs":[],"name":"a","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"calltest1","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"back_manager","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address payable","name":"user_address","type":"address"},{"internalType":"uint256","name":"sequence","type":"uint256"}],"name":"pay","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[],"name":"get_ether","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[],"name":"test1","type":"event"}]')
bytecode = "60806040526001805534801561001457600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550610238806100646000396000f3fe60806040526004361061004a5760003560e01c80630dbe671f1461004c578063160fd2d5146100775780637426ae541461008e578063c4076876146100a5578063fe5782cf146100f3575b005b34801561005857600080fd5b506100616100fd565b6040518082815260200191505060405180910390f35b34801561008357600080fd5b5061008c610103565b005b34801561009a57600080fd5b506100a3610131565b005b6100f1600480360360408110156100bb57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803590602001909291905050506101b2565b005b6100fb610201565b005b60015481565b7f6b59084dfb7dcf1c687dd12ad5778be120c9121b21ef90a32ff73565a36c9cd360405160405180910390a1565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f193505050501580156101af573d6000803e3d6000fd5b50565b8173ffffffffffffffffffffffffffffffffffffffff166108fc6103e883029081150290604051600060405180830381858888f193505050501580156101fc573d6000803e3d6000fd5b505050565b56fea265627a7a72315820272549dae95563090b343e8eeb65b0eb6023d2fd30d40bf411d5e7f89801569764736f6c634300050b0032"

testRopsten = web3.eth.contract(abi=abi,bytecode=bytecode)
transaction = testRopsten.constructor().buildTransaction()
transaction.update({ 'gas' : 2000000 })
transaction.update({ 'nonce' : web3.eth.getTransactionCount('0x3648109582d7DA09D098faB0c8Aaa3543f633E2f') })
private_key = "D522CE6DE0C170EEAB10517605E58FD3789F6784744DA7DBE68818C30145A795"
signed_tx = web3.eth.account.signTransaction(transaction, private_key)
txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
print(txn_receipt)



