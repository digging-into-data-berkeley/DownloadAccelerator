#! /usr/bin/python

""" Download Accelerator

	A Python utility to download files by parsing a csv file
	It uses `aria2` command line download accelerator utility
	For more information on `aria2` refer: http://aria2.sourceforge.net/
"""

__author__ = "Shreyas"
__email__ = "shreyas@ischool.berkeley.edu"
__python_version = 'Python 2.7.3 -- EPD 7.3-2 (32-bit)'

from optparse import OptionParser


def parseInput():
	""" Command Line Input Parsing

		Parse the user input
	"""
	parser = OptionParser()
	parser.add_option('-i', '--input', dest='filepath')
	(option, args) = parser.parse_args()

	if not option.filepath:
		return parser.error('CSV file path not given, use --input="path.to.csv.file.for.download"')

	return {'src': option.filepath}


def main():
	userInput = parseInput()
	print "File path given: %s " % (userInput['src'])


if __name__ == '__main__':
	main()
