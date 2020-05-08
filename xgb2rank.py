#!/usr/bin/python
import xgboost as xgb
from xgboost import DMatrix
from sklearn.datasets import load_svmlight_file


#  This script demonstrate how to do ranking with xgboost.train
x_train, y_train = load_svmlight_file("libsvm_format.train.txt")
x_valid, y_valid = load_svmlight_file("libsvm_format.valid.txt")
x_test, y_test = load_svmlight_file("libsvm_format.test.txt")

group_train = []
with open("group.train.txt", "r") as f:
    data = f.readlines()
    for line in data:
        group_train.append(int(line.split("\n")[0]))

group_valid = []
with open("group.valid.txt", "r") as f:
    data = f.readlines()
    for line in data:
        group_valid.append(int(line.split("\n")[0]))

group_test = []
with open("group.test.txt", "r") as f:
    data = f.readlines()
    for line in data:
        group_test.append(int(line.split("\n")[0]))

train_dmatrix = DMatrix(x_train, y_train)
valid_dmatrix = DMatrix(x_valid, y_valid)
test_dmatrix = DMatrix(x_test)

train_dmatrix.set_group(group_train)
valid_dmatrix.set_group(group_valid)

params = {'objective': 'rank:pairwise', 'eta': 0.1, 'gamma': 1.0,
          'min_child_weight': 0.1, 'max_depth': 6}
xgb_model = xgb.train(params, train_dmatrix, num_boost_round=4,
                      evals=[(valid_dmatrix, 'validation')])
pred = xgb_model.predict(test_dmatrix)
