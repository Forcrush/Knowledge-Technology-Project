# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-05 08:16:17
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-06 08:30:46


from metric import Levenshtein_Distance


# fetch the words in standard dictionary
def get_dic_words(dic_path):
	res = []
	with open(dic_path, 'r') as f:
		for line in f:
			res.extend(line.split())
		return res


# BKTree implement
# ========================================================================
class ResNode(object):
	"""docstring for ClassName"""
	def __init__(self, word, distance):
		self.word = word
		self.distance = distance
		

class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, word):
		self.word = word
		self.child_dic = {}

	def add(self, newword):
		distance = Levenshtein_Distance(newword, self.word)
		if distance == 0:
			return
		keys = self.child_dic.keys()
		if distance in keys:
			self.child_dic[distance].add(newword)
		else:
			self.child_dic[distance] = TreeNode(newword)

	def query(self, targetword, n):
		result = []
		keys = self.child_dic.keys()
		distance = Levenshtein_Distance(targetword, self.word)
		if distance <= n:
			result.append(ResNode(self.word, distance))
		if distance != 0:
			for dis in range(max(1, distance-n), distance+n+1):
				if dis in keys:
					candidate = self.child_dic[dis]
					result += candidate.query(targetword, n)
		return result

	def get_all_word(self):
		result = []
		keys = self.child_dic.keys()
		values = self.child_dic.values()
		result += [node.word for node in values]
		for key in keys:
			candidate = self.child_dic[key]
			result += candidate.get_all_word()
		return result


class BKTree(object):
	"""docstring for BKTree"""
	def __init__(self, rootword):
		self.root = TreeNode(rootword)
	
	def add(self, newword):
		self.root.add(newword)

	def query(self, targetword, n):
		if self.root is None:
			print("The root of BKTree is empty")
			return []
		else:
			queries = self.root.query(targetword, n)
			if len(queries) == 0:
				# print("No matches for", targetword)
				return []
			else:
				queries.sort(key=lambda x:x.distance, reverse=False)
				return queries

	def get_all_word(self):
		if self.root is None:
			print("The root of BKTree is empty")
			return []
		else:
			return self.root.get_all_word()


