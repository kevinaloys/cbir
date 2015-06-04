from descriptor import Descriptor
import glob
import cv2
import argparse

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-d','--dataset', required = True,
	help = 'Path to directory containing the dataset')
argument_parser.add_argument('-i','--index', required = True,
	help = 'Path to save computed index')
args = vars(argument_parser.parse_args())

color_descriptor = Descriptor((8, 12, 3))
number_of_images = len(glob.glob('jpg/*.jpg'))

with open(args['index'], 'w') as output:
	
	for image_path in glob.glob(args['dataset'] + '/*.jpg'):
		image_id = image_path[image_path.rfind('/') + 1:]
		image = cv2.imread(image_path)
		features = color_descriptor.describe(image)
		print('Computing features for image', image_id)
		features = [str(f) for f in features]
		output.write('%s, %s\n' % (image_id,','.join(features)))
		print(str((number_of_images - 1)) + 'left')
		number_of_images = number_of_images - 1