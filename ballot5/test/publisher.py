import json
from web3 import Web3
import time


web3 = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/ws/v3/747b0843f2e04ab7a384fa175deba232"))
web3.eth.defaultAccount = "0x3648109582d7DA09D098faB0c8Aaa3543f633E2f"

address = web3.toChecksumAddress("0x6DF52a59Cb6eEb2406A4846dA82D5e8714e4D0A6")
abi = json.loads('[{"constant":true,"inputs":[],"name":"a","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"calltest1","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"back_manager","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address payable","name":"user_address","type":"address"},{"internalType":"uint256","name":"sequence","type":"uint256"}],"name":"pay","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[],"name":"get_ether","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[],"name":"test1","type":"event"}]')

testRopsten = web3.eth.contract(address=address, abi=abi)

a = testRopsten.functions.a().call()
print(a)
print(type(a))