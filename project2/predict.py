# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-07 12:50:21
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-09 11:29:44


import arff
import numpy as np
import os
import pickle
import csv


def load_data(filename):
	raw_dataset = arff.load(open(filename), encode_nominal=True)
	dataset = np.array(raw_dataset['data'])
	
	tweet_id = dataset[:, 0]
	x_pred = dataset[:, 2:-1]
	y_pred = dataset[:, -1]
	# print(x_pred.shape, y_pred.shape)
	x_pred = x_pred.astype(np.float64)
	y_pred = y_pred.astype(np.float64)

	return tweet_id, x_pred, y_pred


def write_to_csv(tweet_id, y_final_pred):
	# label 0: Newyork 1: California 2: Georgia
	geo = ['NewYork', 'California', 'Georgia']
	with open("tweet_geolocation_prediction.csv", 'w', newline='') as f:
		csv_w = csv.writer(f)
		csv_w.writerow(['tweet-id', 'class'])
		for i in range(len(tweet_id)):
			# tweet_id: str -- '1234.0' => str -- '1234'
			csv_w.writerow([str(int(float(tweet_id[i]))), geo[int(y_final_pred[i])]])


def predict_with_model(fea_c1, fea_c2, model):

	predict_filename = "data/BEST&MOST{}/test-{}{}.arff".format(fea_c2, fea_c1, fea_c2)
	if not os.path.exists(predict_filename):
		print("No such file: {}".format(predict_filename))
		return

	if not os.path.exists("model/{}{}-{}.pkl".format(fea_c1, fea_c2, model)):
		print("No such model: " + "model/{}{}-{}.pkl".format(fea_c1, fea_c2, model))
		return

	tweet_id, x_pred, _ = load_data(predict_filename)

	with open("model/{}{}-{}.pkl".format(fea_c1, fea_c2, model), 'rb') as f:
		mol = pickle.load(f)

	y_final_pred = mol.predict(x_pred)

	write_to_csv(tweet_id, y_final_pred)