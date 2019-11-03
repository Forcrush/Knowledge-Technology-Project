# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-11 20:43:10
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-13 08:40:28

import os
import data_processing as dp
import metric


# evaluate the first task -- judging a blending word
def judge_eval(bktree, filename, limit_type):
	if os.path.exists("evaluation_data/candidates_evaluation.txt"):
		print("Evaluation has been done!\nSee details in candidates_evaluation.txt")
	else:
		new_candidate = []
		hit_num = 0
		with open(filename, 'r') as f:
			for line in f:
				if dp.judge_blend(bktree, line[:-1], limit_type):
					new_candidate.append(line[:-1])
		with open("data/blends.txt", 'r') as f:
			for line in f:
				if line.split()[0] in new_candidate:
					hit_num += 1
		with open("evaluation_data/candidates_evaluation.txt", 'w') as f:
			f.write("Predicated blending words in candidates.txt:\n")
			for i in new_candidate:
				f.write(i+'\n')
			f.write("===============\n")
			f.write("Number of predicated blending words: "+str(len(new_candidate))+'\n')
			f.write("Hitted true blending words in blends.txt: "+str(hit_num)+'\n')


# evaluete the second task -- finding the two components
def components_eval(bktree, filename, limit_type):
	if os.path.exists("evaluation_data/blends_evaluation.txt"):
		print("Evaluation has been done!\nSee details in blends_evaluation.txt")
	else:
		count = 0
		pred = []
		LD_fp_0, LD_sp_0 = 0, 0
		LD_fp_1, LD_sp_1 = 0, 0
		LD_fp_2, LD_sp_2 = 0, 0
		LD_fp_x, LD_sp_x = 0, 0
		with open(filename, 'r') as f:
			for line in f:
				count += 1
				print(count)
				ls = line.split()
				origin, fir_com, sec_com = ls[0], ls[1], ls[2]
				#print(origin, fir_com, sec_com)
				fir_pre, sec_pre = dp.get_two_blends(bktree, origin, limit_type)
				pred.append([origin, fir_pre, sec_pre])
				LD_fp, LD_sp = metric.Levenshtein_Distance(fir_pre, fir_com), metric.Levenshtein_Distance(sec_pre, sec_com)
				if LD_fp == 0:
					LD_fp_0 += 1
				elif LD_fp == 1:
					LD_fp_1 += 1
				elif LD_fp == 2:
					LD_fp_2 += 1
				else:
					LD_fp_x += 1

				if LD_sp == 0:
					LD_sp_0 += 1
				elif LD_sp == 1:
					LD_sp_1 += 1
				elif LD_sp == 2:
					LD_sp_2 += 1
				else:
					LD_sp_x += 1

		with open("evaluation_data/blends_evaluation.txt", 'w') as f:
			for i in pred:
				f.write(i[0]+'\t'+i[1]+'\t'+i[2]+'\n')
			f.write("===============\n")
			f.write("For first component predication:\n")
			f.write("Percentage of LD(Levenshtein Distance) = 0: "+str(LD_fp_0/count)+'\n')
			f.write("Percentage of LD(Levenshtein Distance) = 1: "+str(LD_fp_1/count)+'\n')
			f.write("Percentage of LD(Levenshtein Distance) = 2: "+str(LD_fp_2/count)+'\n')
			f.write("Percentage of LD(Levenshtein Distance) > 2: "+str(LD_fp_x/count)+'\n')
			f.write("For second component predication:\n")
			f.write("Percentage of LD(Levenshtein Distance) = 0: "+str(LD_sp_0/count)+'\n')
			f.write("Percentage of LD(Levenshtein Distance) = 1: "+str(LD_sp_1/count)+'\n')
			f.write("Percentage of LD(Levenshtein Distance) = 2: "+str(LD_sp_2/count)+'\n')
			f.write("Percentage of LD(Levenshtein Distance) > 2: "+str(LD_sp_x/count)+'\n')

