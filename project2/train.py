# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-07 12:50:21
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-08 14:37:09


import arff
import numpy as np
import pickle
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.decomposition import PCA


def load_data(filename):
	raw_dataset = arff.load(open(filename), encode_nominal=True)
	dataset = np.array(raw_dataset['data'])

	x_train = dataset[:, 2:-1]
	y_train = dataset[:, -1]
	# print(x_train.shape, y_train.shape)
	x_train = x_train.astype(np.float64)
	y_train = y_train.astype(np.float64)

	return x_train, y_train


def pca(x_train):
	pca = PCA(n_components=0.95)
	new_x_train = pca.fit_transform(x_train)
	return new_x_train


def train_with_model(fea_c1, fea_c2, model):

	train_filename = "data/BEST&MOST{}/train-{}{}.arff".format(fea_c2, fea_c1, fea_c2)
	if not os.path.exists(train_filename):
		print("No such file: {}".format(train_filename))
		return
	
	if os.path.exists("model/{}{}-{}.pkl".format(fea_c1, fea_c2, model)):
		print("This model had been trained: " + "model/{}{}-{}.pkl".format(fea_c1, fea_c2, model))
	
	else:
	
		x_train, y_train = load_data(train_filename)

		'''
		PCA operation
		print(x_train.shape)
		x_train = pca(x_train)
		print(x_train.shape)
		'''

		if model == 'knn':
			mol = KNeighborsClassifier()
			mol.fit(x_train, y_train)

		elif model == 'rn':
			mol = RadiusNeighborsClassifier(radius=5.0)
			mol.fit(x_train, y_train)

		elif model == 'bnb':
			mol = BernoulliNB()
			mol.fit(x_train, y_train)

		elif model == 'gnb':
			mol = GaussianNB()
			mol.fit(x_train, y_train)

		elif model == 'dtree':
			mol = tree.DecisionTreeClassifier()
			mol.fit(x_train, y_train)

		elif model == 'rdforest':
			mol = RandomForestClassifier(n_estimators=10)
			mol.fit(x_train, y_train)

		elif model == 'lsvc':
			mol = LinearSVC(random_state=0, tol=1e-5)
			mol.fit(x_train, y_train)

		elif model == 'qda':
			mol = QuadraticDiscriminantAnalysis()
			mol.fit(x_train, y_train)


		with open("model/{}{}-{}.pkl".format(fea_c1, fea_c2, model), 'wb') as f:
			pickle.dump(mol, f)