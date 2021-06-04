import numpy as np
from sklearn.linear_model import SGDClassifier

def LR_SGD(X, y, intercept_, coef_):
    """
    :param X: 训练样本
    :param y: 标签
    :param intercept_: 截距
    :param coef_: 模型参数
    :return: intercept_, coef_
    """
    sgd_clf = SGDClassifier(loss="log")
    if len(intercept_) != 0 and len(coef_) != 0:
        sgd_clf.intercept_ = intercept_
        sgd_clf.coef_ = coef_

    sgd_clf.partial_fit(X, y, classes = np.array([0 ,1]))

    return sgd_clf.intercept_, sgd_clf.coef_



def SGD_predict(X, intercept_, coef_, classes_=np.array([0, 1])):
    """
    :param X: 预测数据集
    :param intercept_: 截距
    :param coef_: 模型参数
    :param classes_: 预测类别
    :return:
    """
    sgd_clf = SGDClassifier(loss="log")
    sgd_clf.intercept_ = intercept_
    sgd_clf.coef_ = coef_
    sgd_clf.classes_ = classes_

    y_pred = sgd_clf.predict(X)
    return y_pred

