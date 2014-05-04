#!/usr/bin/env python

from PIL import Image
import argparse, os

def ensure_dir(directoryName):
	if os.path.exists(directoryName):
		return directoryName
	elif not os.path.exists(directoryName):
		convertedDirName = os.getcwd() + '/' + directoryName
		os.makedirs(convertedDirName)
		return os.getcwd() + '/' + directoryName
	else:
		print "Something Bad Happened with the file / directory"


def main ():
	parser = argparse.ArgumentParser(description='Change one or multiple file sizes.')
	parser.add_argument('-s', nargs='+', required=True, metavar='source', dest='source',
	                   help='The file or directory that holds images')
	parser.add_argument('-d', default='reSize', metavar='destination', dest='destination',
	                   help='The location to save new images (default is the reSize directory in current directory)')
	parser.add_argument('-H', default=100, metavar='height', dest='height',
	                   help='The height of the new image(s)')
	parser.add_argument('-w', default=100, metavar='width', dest='width',
	                   help='The width of the new image(s)')

	args = vars(parser.parse_args())

	size = (args['height'], args['width'])

	for key in args['source']:
		if os.path.isdir(key):
			if key == '.':
				flag = 1
				key = os.getcwd()
			for filename in os.listdir(key):
				if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
					try:
						if flag == 1:
							original = Image.open(filename)
						else:
							original = Image.open(str(args['source']).replace("[", '').replace("]",'').replace("'",'') + filename)
						original.thumbnail(size)
						filesplit = os.path.splitext(filename)
						saveLocation = ensure_dir(args['destination'])
						original.save(saveLocation + '/' + filesplit[0] + 'Resized' + filesplit[1])
					except:
						pass
		elif os.path.isfile(key):
			print key
			try:
				original = Image.open(key)
				original.thumbnail(size)
				filesplit = os.path.splitext(key)
				saveLocation = ensure_dir(args['destination'])
				original.save(saveLocation +'/' + filesplit[0] + 'Resized' + filesplit[1])

			except:
				pass
		else:
			print "Something Bad Happend with Pillow"		

if __name__ == "__main__":
	main()

