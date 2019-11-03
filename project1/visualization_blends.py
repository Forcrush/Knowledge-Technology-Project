# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-05 10:00:20
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-06 11:10:02

import textdistance
import matplotlib.pyplot as plt
import numpy as np


# show jaro_winkler similarity between blending word and its two blends respectively
def jaro_winkler_sim_of_blends():
	blend1, blend2 = [], []
	count = 0
	with open("data/blends.txt", 'r') as f:
		for line in f:
			s = line.split()
			origin, first, second = s[0], s[1], s[2]
			blend1.append(textdistance.jaro_winkler(origin,first))
			blend2.append(textdistance.jaro_winkler(origin,second))
			count += 1
	#print(textdistance.jaro_winkler())

	x = np.array([i for i in range(count)])
	y1 = np.array(blend1)
	y2 = np.array(blend2)

	plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)
	plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1)

	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("jaro_winkler similarity", fontsize=12, color='g')
	print("first blend: 0.7 ~ 0.95 / 0.52 ~ 0.65\n second blend: 0.7 ~ 0.95 / 0.4 ~ 0.6/ 0.0")
	plt.show()


# show levenshtein normalized similarity between blending word and its two blends respectively
def levenshtein_sim_of_blends():
	blend1, blend2 = [], []
	count = 0
	with open("data/blends.txt", 'r') as f:
		for line in f:
			s = line.split()
			origin, first, second = s[0], s[1], s[2]
			blend1.append(textdistance.levenshtein.normalized_similarity(origin,first))
			blend2.append(textdistance.levenshtein.normalized_similarity(origin,second))
			count += 1
	#print(textdistance.jaro_winkler())

	x = np.array([i for i in range(count)])
	y1 = np.array(blend1)
	y2 = np.array(blend2)

	plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)
	plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1)

	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("levenshtein normalized similarity",fontsize=12,color='g')
	print("first blend: 0.1 ~ 0.8\nsecond blend: 0.3 ~ 0.9")
	plt.show()


# show ratcliff-obershelp similarity between blending word and its two blends respectively
def ratcliff_obershelp_sim_of_blends():
	blend1, blend2 = [], []
	count = 0
	with open("data/blends.txt", 'r') as f:
		for line in f:
			s = line.split()
			origin, first, second = s[0], s[1], s[2]
			blend1.append(textdistance.ratcliff_obershelp(origin,first))
			blend2.append(textdistance.ratcliff_obershelp(origin,second))
			count += 1
	#print(textdistance.jaro_winkler())

	x = np.array([i for i in range(count)])
	y1 = np.array(blend1)
	y2 = np.array(blend2)

	plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)
	plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1)

	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("ratcliff-obershelp similarity",fontsize=12,color='g')
	print("# first blend: 0.35 ~ 0.85\nsecond blend: 0.45 ~ 0.95")
	plt.show()


# needleman wunsch marks between blending word and its two blends respectively
def needleman_wunsch_of_blends():
	blend1, blend2 = [], []
	count = 0
	with open("data/blends.txt", 'r') as f:
		for line in f:
			s = line.split()
			origin, first, second = s[0], s[1], s[2]
			blend1.append(textdistance.needleman_wunsch(origin,first))
			blend2.append(textdistance.needleman_wunsch(origin,second))
			count += 1
	#print(textdistance.jaro_winkler())

	x = np.array([i for i in range(count)])
	y1 = np.array(blend1)
	y2 = np.array(blend2)

	plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)
	plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1)

	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("needleman_wunsch",fontsize=12,color='g')
	print("first blend: -2.5 ~ 5.0\nsecond blend: 0.0 ~ 8.0")
	plt.show()


# smith waterman marks between blending word and its two blends respectively
def smith_waterman_of_blends():
	blend1, blend2 = [], []
	count = 0
	with open("data/blends.txt", 'r') as f:
		for line in f:
			s = line.split()
			origin, first, second = s[0], s[1], s[2]
			blend1.append(textdistance.smith_waterman(origin,first))
			blend2.append(textdistance.smith_waterman(origin,second))
			count += 1
	#print(textdistance.jaro_winkler())

	x = np.array([i for i in range(count)])
	y1 = np.array(blend1)
	y2 = np.array(blend2)

	plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)
	plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1)

	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("smith_waterman",fontsize=12,color='g')
	print("first blend: 0.0 ~ 0.4\nsecond blend: 0.2 ~ 0.7")
	plt.show()


# gotoh between blending word and its two blends respectively
def gotoh_of_blends():
	blend1, blend2 = [], []
	count = 0
	with open("data/blends.txt", 'r') as f:
		for line in f:
			s = line.split()
			origin, first, second = s[0], s[1], s[2]
			blend1.append(textdistance.gotoh(origin,first))
			blend2.append(textdistance.gotoh(origin,second))
			count += 1
	#print(textdistance.jaro_winkler())

	x = np.array([i for i in range(count)])
	y1 = np.array(blend1)
	y2 = np.array(blend2)

	plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)
	plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1)

	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("gotoh",fontsize=12,color='g')
	print("first blend: -1.5 ~ 5.5\nsecond blend: -1.5 ~ 7.0")
	plt.show()


# strcmp95 between blending word and its two blends respectively
def strcmp95_of_blends():
	blend1, blend2 = [], []
	count = 0
	with open("data/blends.txt", 'r') as f:
		for line in f:
			s = line.split()
			origin, first, second = s[0], s[1], s[2]
			blend1.append(textdistance.strcmp95(origin,first))
			blend2.append(textdistance.strcmp95(origin,second))
			count += 1
	#print(textdistance.jaro_winkler())

	x = np.array([i for i in range(count)])
	y1 = np.array(blend1)
	y2 = np.array(blend2)

	plt.plot(x, y1, color="r", linestyle="-", marker="^", linewidth=1)
	plt.plot(x, y2, color="b", linestyle="-", marker="s", linewidth=1)

	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("strcmp95",fontsize=12,color='g')
	print("first blend: 0.5 ~ 0.7 / 0.75 ~ 0.95\nsecond blend: 0.5 ~ 0.6 / 0.7 ~ 0.95")
	plt.show()


# jaro_winkler_sim_of_blends()
# levenshtein_sim_of_blends()
# ratcliff_obershelp_sim_of_blends()
# needleman_wunsch_of_blends()
# smith_waterman_of_blends()
# gotoh_of_blends()
# strcmp95_of_blends()