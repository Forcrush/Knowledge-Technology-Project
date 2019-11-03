# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-05 18:52:12
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-13 08:51:27

import re
import random
from collections import Counter
import textdistance

import metric


# query a word from bktree, the edit distance is limited in [2, max(2, len(word)//2+1)]
def query_word(bktree, word):
	'''
	# select words has smaller edit-distance
	small_res = bktree.query(word, 1)
	small_set = set()
	for node in small_res:
		small_set.add(node.word)
	'''
	# select words has larger edit-distance
	# large_res = bktree.query(word, max(2, len(word)//2+1))
	large_res = bktree.query(word, len(word)//2+1)
	large_set = set()
	for node in large_res:
		large_set.add(node.word)
	'''
	# edit-distance between word and each item in final set is in 1 < dis <= max(2, len(word)//2)
	return list(large_set - small_set)
	'''
	return list(large_set)


# given a word 'axxxxb', find words like 'a...' or '...b'
def head_tail_match(word, word_list):
	if len(word) == 1 or word_list == []:
		return []
	head, tail = word[0], word[-1]
	pattern1 = '^' + head
	pattern2 = '.*' + tail + '$'
	head_match = []
	tail_match = []
	for w in word_list:
		if re.match(pattern1, w):
			head_match.append(w)
		if re.match(pattern2, w):
			tail_match.append(w)
	return head_match, tail_match


def filter_blends(word, first_blend, second_blend, limit="1237"):
	refined_first_blend, refined_second_blend = [], []
	for w in first_blend:
		qua1 = metric.qualified("jw_sim", textdistance.jaro_winkler(word, w), True, False)
		qua2 = metric.qualified("levenshtein_sim", textdistance.levenshtein.normalized_similarity(word, w), True, False)
		qua3 = metric.qualified("ro_sim", textdistance.ratcliff_obershelp(word, w), True, False)
		qua4 = metric.qualified("needleman_wunsch", textdistance.needleman_wunsch(word, w), True, False)
		qua5 = metric.qualified("smith_waterman", textdistance.smith_waterman(word, w), True, False)
		qua6 = metric.qualified("gotoh", textdistance.gotoh(word, w), True, False)
		qua7 = metric.qualified("strcmp95", textdistance.strcmp95(word, w), True, False)
		metric_pool = [qua1, qua2, qua3, qua4, qua5, qua6, qua7]
		statis = True
		for i in limit:
			statis &= metric_pool[int(i)-1]
		if statis:
			refined_first_blend.append(w)

	for w in second_blend:
		qua1 = metric.qualified("jw_sim", textdistance.jaro_winkler(word, w), False, True)
		qua2 = metric.qualified("levenshtein_sim", textdistance.levenshtein.normalized_similarity(word, w), False, True)
		qua3 = metric.qualified("ro_sim", textdistance.ratcliff_obershelp(word, w), False, True)
		qua4 = metric.qualified("needleman_wunsch", textdistance.needleman_wunsch(word, w), False, True)
		qua5 = metric.qualified("smith_waterman", textdistance.smith_waterman(word, w), False, True)
		qua6 = metric.qualified("gotoh", textdistance.gotoh(word, w), False, True)
		qua7 = metric.qualified("strcmp95", textdistance.strcmp95(word, w), False, True)
		metric_pool = [qua1, qua2, qua3, qua4, qua5, qua6, qua7]
		statis = True
		for i in limit:
			statis &= metric_pool[int(i)-1]
		if statis:
			refined_second_blend.append(w)

	return refined_first_blend, refined_second_blend


'''
under limit: 1237 : qua1 && qua2 && qua3 && qua7
a[i]: len(refined_first_blend) and b[i]: len(refined_second_blend) for each blending word in blends.txt
c[i]: the proportion relationship between a and b

a = [1096, 1707, 734, 411, 1797, 186, 1036, 322, 322, 607, 1741, 1594, 1014, 1032, 486, 1031, 1132, 507, 748, 719, 649, 1158, 866, 1070, 766, 786, 1165, 577, 608, 1011, 1056, 529, 1270, 336, 421, 197, 417, 428, 722, 929, 420, 859, 62, 178, 198, 638, 391, 41, 272, 823, 262, 1178, 408, 945, 1093, 359, 804, 599, 394, 1083, 429, 132, 451, 319, 674, 138, 374, 460, 310, 192, 195, 85, 118, 348, 175, 279, 515, 529, 474, 395, 790, 483, 1312, 789, 772, 241, 1146, 1219, 863, 495, 438, 849, 465, 483, 515, 571, 691, 701, 858, 910, 476, 745, 258, 374, 159, 524, 351, 117, 1595, 665, 1270, 1082, 2141, 552, 540, 1643, 818, 1341, 1214, 691, 452, 1108, 747, 1303, 941, 553, 1097, 1278, 1100, 826, 1919, 2529, 1296, 1178, 875, 1148, 923, 666, 1589, 1314, 802, 598, 593, 881, 948, 1035, 924, 874, 1278, 952, 779, 1324, 1040, 1378, 974, 762, 534, 699, 512, 318, 667, 600, 497, 440, 643, 245, 438, 660, 247, 294, 319, 97, 326, 231, 307, 466, 782, 94, 202, 232, 225, 71, 126] 
b = [208, 372, 233, 47, 820, 190, 500, 259, 490, 44, 304, 954, 291, 356, 924, 366, 513, 153, 20, 281, 137, 861, 314, 463, 688, 472, 165, 120, 1411, 204, 507, 263, 891, 616, 589, 466, 52, 45, 332, 477, 94, 409, 17, 65, 169, 197, 349, 208, 244, 240, 815, 328, 588, 207, 732, 50, 650, 293, 303, 688, 237, 98, 302, 188, 316, 151, 390, 539, 1126, 328, 276, 17, 253, 311, 42, 683, 392, 403, 465, 129, 483, 566, 468, 398, 175, 155, 268, 588, 559, 257, 78, 402, 46, 173, 196, 248, 70, 843, 320, 366, 214, 331, 116, 1158, 116, 337, 335, 96, 588, 284, 422, 919, 1160, 297, 304, 764, 491, 410, 293, 88, 356, 284, 188, 1815, 90, 78, 411, 382, 155, 109, 830, 1065, 371, 128, 102, 265, 262, 66, 586, 614, 258, 197, 209, 58, 177, 231, 161, 350, 478, 133, 120, 375, 19, 464, 398, 298, 40, 1387, 251, 324, 197, 289, 87, 439, 155, 52, 85, 29, 112, 476, 430, 57, 210, 202, 411, 70, 753, 71, 203, 189, 189, 177, 79]
import matplotlib.pyplot as plt
import numpy as np
c = [a[i]/b[i] for i in range(len(a))]
x = np.array([i for i in range(len(a))])
y1 = np.array(a)
y2 = np.array(b)
y3 = np.array(c)
#plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)
#plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1)
plt.plot(x, y3, color="r", linestyle="-", marker="^", linewidth=1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("xxxx",fontsize=12,color='g')
plt.show()
'''

def get_blend_component(bktree, word, limit):
		first_blend, second_blend = head_tail_match(word, query_word(bktree, word))
		flt_fir_b, fil_sec_b = filter_blends(word, first_blend, second_blend, limit)
		return flt_fir_b, fil_sec_b


# too many same characters in one word
def duplicate_cha(word):
	if len(word) <= 2:
		return True
	# find countinuous repeating character
	for i in range(97, 123):
		if re.match('.*('+chr(i)+'){3,}.*', word):
			return True
	c = Counter(word)
	if len(word) <= 3:
		if len(c) == 1:
			return True
	elif len(word) <= 5:
		for value in c.values():
			if value >= 3:
				return True
	elif len(word) >= 9:
		if len(c) <= 4:
			return True
		for value in c.values():
			if value >= len(word)//3+1:
				return True
	else:
		for value in c.values():
			if value >= len(word)//2:
				return True
	return False


# to judge whether a word is a blending word
def judge_blend(bktree, word, limit):
	# too many same character
	if duplicate_cha(word):
		return False
	candidates = query_word(bktree, word)
	if candidates == []:
		return False
	'''
	this condition will eliminate the word in dictionary
	since we are judging word from candidatex.txt (has already been cleaned)
	so there is need to add the 'if' condition (if we use the origin text, this condition is necessary)
	'''
	# word in dictionary
	if word in candidates:
		return False
	else:
		first_blend, second_blend = head_tail_match(word, candidates)
		re_fir_ble, re_sec_ble = filter_blends(word, first_blend, second_blend, limit)
		# 10 contains most situations (blends.txt), details in data_processing.py
		if len(re_fir_ble) == 0 or len(re_sec_ble) == 0:
			return False
		if len(re_fir_ble) / len(re_sec_ble) < 10:
			print(word)
			return True
	return False


# to get two components of a blending word
def get_two_blends(bktree, word, limit):
	re_fir_ble, re_sec_ble = get_blend_component(bktree, word, limit)
	for i in re_fir_ble:
		if duplicate_cha(i):
			re_fir_ble.remove(i)
	for i in re_sec_ble:
		if duplicate_cha(i):
			re_sec_ble.remove(i)
	if len(re_fir_ble) == 0 or len(re_sec_ble) == 0:
		return None, None
	re_fir_ble.sort()
	re_sec_ble.sort()
	if len(word) <= 6:
		defined_dis = 1
		while defined_dis <= 3:
			start, end = 1, len(word)-2
			flag_fir, flag_sec = False, False
			fir_com, sec_com = '', ''

			while start <= end:
				for sec in re_sec_ble:
					if re.match('.*'+word[start:]+'$', sec) and metric.Levenshtein_Distance(sec, word[start:]) == defined_dis:
						flag_sec = True
						sec_com = sec
						break
				if flag_sec:
					for fir in re_fir_ble:
						if re.match('^'+word[:start], fir) and metric.Levenshtein_Distance(fir, word[:start]) >= 2*len(word[:start]):
							flag_fir = True
							fir_com = fir
							break
				# can not find proper second component
				else:
					start += 1
					continue
				if flag_fir:
					return fir_com, sec_com
				# can not find proper first component
				else:
					# relaxation condition
					for fir in re_fir_ble:
						if re.match('^'+word[:start], fir):
							flag_fir = True
							fir_com = fir
							break
					if flag_fir:
						return fir_com, sec_com
					# more relaxation condition
					else:
						fir_com = re_fir_ble[random.randint(0, len(re_fir_ble)-1)]
						return fir_com, sec_com

			# can not find proper second component the whole process under current defined_dis
			defined_dis += 1
		
		# randomly choosing
		fir_com = re_fir_ble[random.randint(0, len(re_fir_ble)-1)]
		sec_com = re_sec_ble[random.randint(0, len(re_sec_ble)-1)]
		
		return fir_com, sec_com

	else:
		defined_dis = 0
		while defined_dis <= 3:
			start, middle = len(word)//2+1, len(word)//2+1
			count = 0
			flag_fir, flag_sec = False, False
			fir_com, sec_com = '', ''

			while 1 <= start <= len(word)-1:
				for fir in re_fir_ble:
					if re.match('^'+word[:start], fir) and metric.Levenshtein_Distance(fir, word[:start]) <= defined_dis:
						flag_fir = True
						fir_com = fir
						break
				if flag_fir:
					for sec in re_sec_ble:
						if re.match('.*'+word[start:]+'$', sec) and metric.Levenshtein_Distance(sec, word[start:]) >= 2:
							flag_sec = True
							sec_com = sec
							break
				# can not find proper second component
				else:
					count += 1
					if count % 2 == 0:
						start = middle + count // 2
					else:
						start = middle - (count + 1) // 2
					continue
				if flag_sec:
					return fir_com, sec_com
				# can not find proper first component
				else:
					# relaxation condition
					for sec in re_sec_ble:
						if re.match('.*'+word[start:]+'$', sec):
							flag_fir = True
							sec_com = sec
							break
					if flag_sec:
						return fir_com, sec_com
					# more relaxation condition
					else:
						sec_com = re_sec_ble[random.randint(0, len(re_sec_ble)-1)]
						return fir_com, sec_com

			# can not find proper second component the whole process under current defined_dis
			defined_dis += 1
		
		# randomly choosing
		fir_com = re_fir_ble[random.randint(0, len(re_fir_ble)-1)]
		sec_com = re_sec_ble[random.randint(0, len(re_sec_ble)-1)]
		
		return fir_com, sec_com

