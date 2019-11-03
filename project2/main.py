# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-07 11:42:13
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-12 11:05:44


from tqdm import trange
import train, evaluate, predict


def main():

	fea_number = ["10", "20", "50", "200"]
	fea_choice = ["most", "best"]
	model = ["knn", "gnb", "dtree", "rdforest", "lsvc", "qda"]
	# c1, c2, c3 = 0, 0, 0

	flag = True

	# training and evaluation
	if flag:
		total_steps = len(fea_number) * len(fea_choice) * len(model)
		for step in trange(total_steps):
			c2 = step // (len(fea_choice) * len(model))
			c1 = (step // len(model)) % len(fea_choice)
			c3 = step % len(model)

			# train (based on data/BEST&MOSTXX/train-xxx.arff)
			train.train_with_model(fea_choice[c1], fea_number[c2], model[c3])

			# evaluate (based on data/BEST&MOSTXX/dev-xxx.arff)
			evaluate.evaluate_with_model(fea_choice[c1], fea_number[c2], model[c3])
	
	# prediction
	else:
		# predict (based on data/BEST&MOSTXX/test-xxx.arff)
		# the parameters should be selected from the result of training and evaluation process
		predict.predict_with_model('best', '200', 'lsvc')


if __name__ == '__main__':
	main()