import csv
import numpy

class Search:

	def __init__(self, index_path):
		self.index_path = index_path


	def search(self, query_features, number_of_results = 10):
		results = {}
		with open(self.index_path,'r') as f:
			read = csv.reader(f)
			for row in read:
				features = [float(feature) for feature in row[1:]]
				distance = self.chi_squared_distance(features, query_features)
				results[row[0]] = distance
		results = sorted([(value, key) for (key, value) in results.items()])
		return results[:number_of_results]


	def chi_squared_distance(self, histogram_A, histogram_B, eps = 1e-10):
		distance = 0.5 * numpy.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histogram_A, histogram_B)])
		return distance