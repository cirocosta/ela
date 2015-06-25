#!/usr/bin/python

from __future__ import print_function
from PIL import Image
import os
import sys


# remember: PIL quality of JPEG compression lets
#						us go from 1 to 95
def imgcomp(src, times=20, quality=50):
	"""
	Compresses a given image for a given amount of
	time.
	"""
	directory, fname = os.path.split(src)
	name, _ = os.path.splitext(fname)
	gen_directory = os.path.join(directory, "generated")
	BASENAME = os.path.join(gen_directory, name)

	if not os.path.exists(gen_directory):
		os.makedirs(gen_directory)
	last_src = src

	try:
		for n in xrange(1, times+1):
			new_src = "%s_%.2d.jpg" % (BASENAME, n)
			new_image = Image.open(last_src)
			quality -= 1
			new_image.save(new_src, "JPEG", quality=quality, \
										 optimize=False, progressive=False)
			last_src = new_src
	except IOError:
		print("Error in %r" % src)
		raise


def main():
	imgcomp("../assets/square3.jpg")


if __name__ == '__main__':
	main()
else:
	print("This shouldn't be imported.", file=sys.stderr)
	sys.exit(1)

