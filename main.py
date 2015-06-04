from descriptor import Descriptor
from search import Search
import glob
import cv2
import argparse

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-i','--index', required = True,
	help = 'Path to save computed index')
argument_parser.add_argument('-q','--query', required = True,
	help = 'Path to query image')
argument_parser.add_argument('-d','--dataset', required = True,
	help = 'Path to result')
args = vars(argument_parser.parse_args())

color_descriptor = Descriptor((8, 12, 3))

query_image = cv2.imread(args['query'])
query_feature = color_descriptor.describe(query_image)
searcher = Search(args['index'])
feature_result = searcher.search(query_feature)

cv2.imshow('Query Image', query_image)

for score, image_name in feature_result:
	result = cv2.imread(args['dataset'] + '/' + image_name)
	cv2.imshow('Best Matching', result)
	cv2.waitKey(0)