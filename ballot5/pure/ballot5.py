import sys
import json
from web3 import Web3
import time
from constants import const
from LR_SGD import LR_SGD
from LR_SGD import SGD_predict
import numpy as np

account_number = int(sys.argv[1])
account_address = sys.argv[2]
account_private_key = sys.argv[3]

# web3 = Web3(Web3.HTTPProvider(const.GANACHE_URL))
web3 = Web3(Web3.WebsocketProvider(const.GANACHE_URL))
web3.eth.defaultAccount = account_address

address = web3.toChecksumAddress(const.CONTRACT_ADDRESS)
abi = json.loads(const.ABI)
Ballot5 = web3.eth.contract(address=address, abi=abi)

dataset = np.loadtxt('E:/Data/creditcard/creditcard.csv', delimiter=",")
X = dataset[:, 1:-2]
y = dataset[:, -1]

X_train = X[account_number*2000 : (account_number+1)*2000]
y_train = y[account_number*2000 : (account_number+1)*2000]

if X_train.ndim == 1:
    X_train = X_train.reshape(1, -1)
    y_train = np.array([y_train])

states = dict()
states['start'] = 0
states['download_param'] = 0
states['vote_statistics_complete'] = 0
states['end'] = 0

def monitor_event(state, poll_interval):
    while True:
        tmp = -1
        if state == 'start':
            if Ballot5.functions.start().call() == 1:
                print("state:start monitored")
                return
        elif state == 'end':
            if Ballot5.functions.end().call() == 1:
                print("state:end monitored")
                return
        elif state == 'download_param':
            tmp = Ballot5.functions.download_param().call()
        elif state == 'vote_statistics_complete':
            tmp = Ballot5.functions.vote_statistics_complete().call()
        if states[state] + 1 == tmp:
            states[state] = tmp
            print("user:%d state:%s monitored"%(account_number, state))
            return
        time.sleep(poll_interval)

print("用户%d完成数据加载, 准备接入到训练中" % (account_number))

while True:
    coef = Ballot5.functions.valid_coef().call()
    intercept = Ballot5.functions.valid_intercept().call()
    print("用户%d获取初始化参数成功"%(account_number))

    if coef != "" and intercept != "":
        try:
            coef = coef.split(',')
            coef = np.array(list(map(float, coef))).reshape(1, -1)
            intercept = np.array([float(intercept)])
        except Exception as e:
            print("Error:", e)
            print("coef: %s" % (coef))
            print("intercept: %s" % (intercept))

    intercept, coef = LR_SGD(X_train, y_train, intercept, coef)
    intercept_str = intercept[0].__str__()
    coef_str = ','.join(i.__str__() for i in coef[0])

    transaction = Ballot5.functions.upload_param(intercept_str, coef_str).buildTransaction()
    transaction.update({'gas': 1000000})
    transaction.update({'gasPrice': web3.eth.gasPrice * 2})
    transaction.update({'nonce': web3.eth.getTransactionCount(web3.eth.defaultAccount)})
    signed_tx = web3.eth.account.signTransaction(transaction, account_private_key)
    txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    try:
        txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        if txn_receipt['status'] == 1:
            print("user %d upload_param successed. txn_hash: %s" % (account_number, txn_hash.hex()))
        elif txn_receipt['status'] == 0:
            print("user %d upload_param error with status = 0" % (account_number))
    except Exception as e:
        print("Exception:", e)
        print("user: %d, txn_hash: %s" % (account_number, txn_hash.hex()))
        exit()
    print("用户%d上传参数成功" % (account_number))

    monitor_event('download_param', 1)

    intercept_str = Ballot5.functions.getAllIntercept().call()
    coef_str = Ballot5.functions.getAllCoef().call()

    coefs = coef_str.split(';')
    intercepts = intercept_str.split(';')
    votes = ""
    for i in range(len(coefs)):
        coef = coefs[i].split(',')
        coef = np.array(list(map(float, coef))).reshape(1, -1)
        intercept = np.array([float(intercepts[i])])
        y_pred = SGD_predict(X_train, intercept, coef)
        votes += (y_train == y_pred).sum().__str__()
        votes += ","
    if len(votes) != 0:
        votes = votes[0:-1]

    transaction = Ballot5.functions.vote(votes).buildTransaction()
    transaction.update({'gas': 1000000})
    transaction.update({'gasPrice': web3.eth.gasPrice * 2})
    transaction.update({'nonce': web3.eth.getTransactionCount(web3.eth.defaultAccount)})
    signed_tx = web3.eth.account.signTransaction(transaction, account_private_key)
    txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    try:
        txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        if txn_receipt['status'] == 1:
            print("user %d vote successed. txn_hash: %s" % (account_number, txn_hash.hex()))
        elif txn_receipt['status'] == 0:
            print("user %d vote error with status = 0" % (account_number))
    except Exception as e:
        print("Exception:", e)
        print("user: %d, txn_hash: %s" % (account_number, txn_hash.hex()))
        exit()

    print("account:%d address:%s vote:%s completed" % (account_number, account_address, votes))

    monitor_event('vote_statistics_complete', 1)
    curr_beneficiary = Ballot5.functions.curr_beneficiary().call()
    if(curr_beneficiary == web3.eth.defaultAccount):
        print("账户地址为", web3.eth.defaultAccount, "的用户数据已被采用，退出训练")
        break

monitor_event('end', 1)
print("所有参数更新完毕，可以从智能合约中获取参数开始进行预测")

