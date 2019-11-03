# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-05 09:43:03
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-12 17:48:49

import textdistance


def Levenshtein_Distance(s1, s2):
	l1, l2 = len(s1), len(s2)
	matrix = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

	# Action Cost
	match = 0
	delete, insert, replace = 1, 1, 1

	for i in range(1, len(s1)+1):
		matrix[i][0] = i
	for j in range(1, len(s2)+1):
		matrix[0][j] = j

	for i in range(1, len(s1)+1):
		for j in range(1, len(s2)+1):
			# match
			if s1[i-1] == s2[j-1]:
				matrix[i][j] = matrix[i-1][j-1] + match
			else:
				matrix[i][j] = min(matrix[i-1][j]+insert, matrix[i][j-1]+delete, matrix[i-1][j-1]+replace)
	
	return matrix[len(s1)][len(s2)]


def Needle_Wunsch(s1, s2):
	l1, l2 = len(s1), len(s2)
	matrix = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

	# Action Cost
	match = 1
	delete, insert, replace = -1, -1, -1
	"""
	当 match = 0
	delete, insert, replace = 1, 1, 1 时
	最终结果就是 Levenshitein 距离
	"""
	for i in range(1, len(s1)+1):
		matrix[i][0] = i * insert
	for j in range(1, len(s2)+1):
		matrix[0][j] = j * delete

	for i in range(1, len(s1)+1):
		for j in range(1, len(s2)+1):
			# match
			if s1[i-1] == s2[j-1]:
				matrix[i][j] = matrix[i-1][j-1] + match
			else:
				# max(insert, delete, replace)
				# min(insert, delete, replace) if match < insert, delete, replace
				matrix[i][j] = max(matrix[i-1][j]+insert, matrix[i][j-1]+delete, matrix[i-1][j-1]+replace)
	
	return matrix[len(s1)][len(s2)]


def Smith_Waterman(s1, s2):
	l1, l2 = len(s1), len(s2)
	matrix = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

	# Action Cost
	match = 1
	delete, insert, replace = -1, -1, -1

	maxval = 0
	for i in range(1, len(s1)+1):
		for j in range(1, len(s2)+1):
			# match
			if s1[i-1] == s2[j-1]:
				matrix[i][j] = matrix[i-1][j-1] + match
			else:
				# max(0, insert, delete, replace)
				# min(0, insert, delete, replace) if match < insert, delete, replace
				matrix[i][j] = max(0, matrix[i-1][j]+insert, matrix[i][j-1]+delete, matrix[i-1][j-1]+replace)
			maxval = max(maxval, matrix[i][j])

	return maxval


'''
to ensure the jaro_winkler_sim/ratcliff_obershelp_sim/... between two words satisfies the 
interval which is extracted from standard blends.txtdemonstrated in visualization_blends.py
'''
def qualified(algorithm, sim, first_part=False, sencond_part=False):
	if algorithm == 'jw_sim':
		if first_part:
			if (0.7 <= sim <= 0.95) or (0.52 <= sim <= 0.65):
				return True
			else:
				return False
		if sencond_part:
			if (0.7 <= sim <= 0.95) or (0.4 <= sim <= 0.6) or (sim == 0):
				return True
			else:
				return False
	elif algorithm == 'levenshtein_sim':
		if first_part:
			if (0.1 <= sim <= 0.8):
				return True
			else:
				return False
		if sencond_part:
			if (0.3 <= sim <= 0.9):
				return True
			else:
				return False
	elif algorithm == 'ro_sim':
		if first_part:
			if (0.35 <= sim <= 0.85):
				return True
			else:
				return False
		if sencond_part:
			if (0.45 <= sim <= 0.95):
				return True
			else:
				return False
	elif algorithm == 'needleman_wunsch':
		if first_part:
			if (-2.5 <= sim <= 5.0):
				return True
			else:
				return False
		if sencond_part:
			if (0.0 <= sim <= 8.0):
				return True
			else:
				return False
	elif algorithm == 'smith_waterman':
		if first_part:
			if (0.0 <= sim <= 0.4):
				return True
			else:
				return False
		if sencond_part:
			if (0.2 <= sim <= 0.7):
				return True
			else:
				return False
	elif algorithm == 'gotoh':
		if first_part:
			if (-1.5 <= sim <= 5.5):
				return True
			else:
				return False
		if sencond_part:
			if (-1.5 <= sim <= 7.0):
				return True
			else:
				return False
	elif algorithm == 'strcmp95':
		if first_part:
			if (0.5 <= sim <= 0.7) or (0.75 <= sim <= 0.95):
				return True
			else:
				return False
		if sencond_part:
			if (0.5 <= sim <= 0.6) or (0.7 <= sim <= 0.95):
				return True
			else:
				return False
	return False

