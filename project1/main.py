# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-04 19:28:01
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-13 09:26:36

import os
from datetime import datetime
import pickle
from tqdm import trange

import metric
import util
import data_processing as dp
import evaluation as eva


bktree_path = "bktree.pkl"
dic_path = "data/dict.txt"
blends_path = "data/blends.txt"
candidates_form = "data/candidates.txt"
# can be as any combination whose each number less than 8 and larger than 0, details in data_processing.py
limit_type = "1237"


def save(bktree, bktree_path):
	with open(bktree_path, 'wb') as f:
		pickle.dump(bktree, f)


def load(bktree_path):
	if os.path.exists(bktree_path):
		print("Loading BKTree...")
		with open(bktree_path, 'rb') as f:
			return pickle.load(f)
	else:
		word_list = util.get_dic_words(dic_path)
		randint = random.randint(0, len(word_list)-1)
		bktree = util.BKTree(word_list[randint])
		print("Buliding BKTree...")
		start = datetime.now()
		for i in trange(len(word_list)):
			bktree.add(word_list[i])
		end = datetime.now() - start
		print("Buliding time:", end)
		# Buliding time: 0:06:54.833567
		save(bktree, bktree_path)
		return bktree


def main():
	
	bktree = load(bktree_path)
	
	# if you want to try a new word, please set evaluation = False
	evaluation = False

	if not evaluation:
		# task1 and task2, you can test any word
		word = input("Judge a word whether a blending word and find the two components of a word, you can test any word\nInput your word: ")
		flag = dp.judge_blend(bktree, word, limit_type)
		if flag:
			print("Maybe a blending word, its two components:")
			print(dp.get_two_blends(bktree, word, limit_type))
		else:
			print("NOT a blending word !")
	else:
		# evaluate task 1
		eva.judge_eval(bktree, candidates_form, limit_type)
		# evaluate task 2
		eva.components_eval(bktree, blends_path, limit_type)


if __name__ == '__main__':
	main()
