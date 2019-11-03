# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-07 12:50:21
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-08 13:37:41


import arff
import numpy as np
import os
import pickle
from sklearn import metrics


def load_data(filename):
	raw_dataset = arff.load(open(filename), encode_nominal=True)
	dataset = np.array(raw_dataset['data'])

	x_eval = dataset[:, 2:-1]
	y_eval = dataset[:, -1]
	# print(x_eval.shape, y_eval.shape)
	x_eval = x_eval.astype(np.float64)
	y_eval = y_eval.astype(np.float64)

	return x_eval, y_eval


def evaluate_with_model(fea_c1, fea_c2, model):

	eval_filename = "data/BEST&MOST{}/dev-{}{}.arff".format(fea_c2, fea_c1, fea_c2)
	if not os.path.exists(eval_filename):
		print("No such file: {}".format(eval_filename))
		return
	
	if not os.path.exists("model/{}{}-{}.pkl".format(fea_c1, fea_c2, model)):
		print("No such model: " + "model/{}{}-{}.pkl".format(fea_c1, fea_c2, model))
		return

	x_eval, y_eval = load_data(eval_filename)

	with open("model/{}{}-{}.pkl".format(fea_c1, fea_c2, model), 'rb') as f:
		mol = pickle.load(f)

	y_pred = mol.predict(x_eval)

	prec = metrics.precision_score(y_eval, y_pred, average='micro')
	recall = metrics.recall_score(y_eval, y_pred, average='micro')
	f1 = 2 * prec * recall / (prec + recall)

	print("{}{}-{}: precision:{:.2f} recall:{:.2f} f1:{:.2f}".format(fea_c1, fea_c2, model, prec, recall, f1))
	with open("result.txt", 'a') as f:
		f.write("{}{}-{}: precision:{:.2f} recall:{:.2f} f1:{:.2f}".format(fea_c1, fea_c2, model, prec, recall, f1) +'\n')