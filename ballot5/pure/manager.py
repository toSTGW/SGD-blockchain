import sys
import json
from web3 import Web3
import time
from constants import const
import numpy as np
from sklearn import model_selection
from LR_SGD import SGD_predict
from sklearn import metrics

valid_user_num = int(sys.argv[1])

web3 = Web3(Web3.WebsocketProvider(const.GANACHE_URL))
# web3 = Web3(Web3.HTTPProvider(const.GANACHE_URL))

address = web3.toChecksumAddress(const.CONTRACT_ADDRESS)
abi = json.loads(const.ABI)
Ballot5 = web3.eth.contract(
    address=const.CONTRACT_ADDRESS,
    abi=abi
)

# metaMask 中的第一个账户
account_address = "0x3648109582d7DA09D098faB0c8Aaa3543f633E2f"
account_private_key = "D522CE6DE0C170EEAB10517605E58FD3789F6784744DA7DBE68818C30145A795"

# metaMask 中的第二个账户
# account_address = "0x5F092a084e5CB8C65b4Cf52DA88d230B5DfE9F62"
# account_private_key = "20F7949473CEBC05BBAD4590FF00569B1C1DD4D9451E14C781BF08ADD831C85F"

#ganache中的账户
# account_address = "0xB59Ca9B4D4BBA3C682Bc60f99cdab41f0E85Ae94"
# account_private_key = "16ca66538471560aaf3979ac20f8fdd0f42fac967a99f55d67670ab403f714a8"

web3.eth.defaultAccount = account_address

"""
Manager running process:
manager: start(valid_user_num)
for i in range(valid_user_num):
    wait for vote_upload_complete() state
    call the 'vote_statics' function to count votes -> send 'vote_statistics_complete()' state
智能合约的发布者需要向智能合约中存入足够的以太币，用以奖励参与训练过程的用户
"""

train_value = 0.01
transaction = Ballot5.fallback().buildTransaction()
transaction.update({'nonce': web3.eth.getTransactionCount(account_address)})
transaction.update({'gas': 100000})
transaction.update({'gasPrice': web3.eth.gasPrice * 3})
transaction.update({'value': web3.toWei(train_value, 'ether')})
signed_tx = web3.eth.account.signTransaction(transaction, account_private_key)
txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
print("已经在合约中存入%f Ether作为奖励" % (train_value))

transaction = Ballot5.functions.mstart(valid_user_num).buildTransaction()
transaction.update({'nonce': web3.eth.getTransactionCount(account_address)})
transaction.update({'gas': 2000000})
transaction.update({'gasPrice': web3.eth.gasPrice * 3})
signed_tx = web3.eth.account.signTransaction(transaction, account_private_key)
txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
if txn_receipt['status'] == 0:
    print("mstart error with status = 0")

states = dict()
states['param_upload_complete'] = 0
states['vote_upload_complete'] = 0
states['download_param'] = 0
states['vote_statistics_complete'] = 0

def monitor_event(state, poll_interval):
    while True:
        tmp = -1
        if state == 'param_upload_complete':
            tmp = Ballot5.functions.param_upload_complete().call()
        elif state == 'vote_upload_complete':
            tmp = Ballot5.functions.vote_upload_complete().call()
        if states[state] + 1 == tmp:
            states[state] = tmp
            print("state:%s monitored"%(state))
            return
        time.sleep(poll_interval)

start_time = time.time()
print("合约初始化完成，等待用户上传参数")
for i in range(valid_user_num):
    s_time = time.time()
    #等待所有用户上传参数
    monitor_event('param_upload_complete', 1)

    #将所有用户上传的参数拼接为一个字符串，供用户下载使用
    while True:
        try:
            transaction = Ballot5.functions.concatInterceptAndCoef().buildTransaction()
            transaction.update({'gasPrice': web3.eth.gasPrice * 3})
            transaction.update({'nonce': web3.eth.getTransactionCount(account_address)})
            transaction.update({'gas': 8000000})
            signed_tx = web3.eth.account.signTransaction(transaction, account_private_key)
            txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
            if txn_receipt['status'] == 1:
                print("concatInterceptAndCoef successed. txn_hash: %s" % (txn_hash.hex()))
            elif txn_receipt['status'] == 0:
                print("concatInterceptAndCoef error with status = 0")
            break
        except Exception as e:
            print("Error:", e)
            print("重试该交易，当前失败的交易hash为:%s" % (txn_hash.hex()))

    monitor_event('vote_upload_complete', 1)

    while True:
        try:
            transaction = Ballot5.functions.vote_statistics().buildTransaction()
            transaction.update({'gasPrice': web3.eth.gasPrice * 3})
            transaction.update({'nonce': web3.eth.getTransactionCount(account_address)})
            transaction.update({'gas': 3000000})
            signed_tx = web3.eth.account.signTransaction(transaction, account_private_key)
            txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
            if txn_receipt['status'] == 1:
                print("vote_statistics successed. txn_hash: %s" % (txn_hash.hex()))
            elif txn_receipt['status'] == 0:
                print("vote_statistics error with status = 0")
            break
        except Exception as e:
            print("Error:", e)
            print("重试该交易，当前失败的交易hash为:%s" % (txn_hash.hex()))

    e_time = time.time()
    print("第%d轮训练用时%d秒" % (i, e_time - s_time))

print("所有用户退出训练")

end_time = time.time()

print("训练结束，共计用时%d秒" % (end_time - start_time))

print("测试训练结果")
dataset = np.loadtxt('E:/Data/creditcard/creditcard.csv', delimiter=",")
X = dataset[:, 1:-2]
y = dataset[:, -1]
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=0)

coef = Ballot5.functions.valid_coef().call()
intercept = Ballot5.functions.valid_intercept().call()
if coef != "" and intercept != "":
    coef = coef.split(',')
    coef = np.array(list(map(float, coef))).reshape(1, -1)
    intercept = np.array([float(intercept)])
y_pred = SGD_predict(X_test,intercept,coef)

print(metrics.confusion_matrix(y_test, y_pred))
print(metrics.classification_report(y_test, y_pred))