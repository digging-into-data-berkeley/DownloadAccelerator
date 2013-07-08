#! /usr/bin/python

""" File Statistics

	Generate File Statistics on a given directory
	to enable estimation for Digging into Data project
"""

__author__ = "Shreyas"
__email__ = "shreyas@ischool.berkeley.edu"
__python_version = "Python 2.7.3 -- EPD 7.3-2 (32-bit)"

from os import listdir
from os import stat
from optparse import OptionParser
from pandas import Series


def getInput():
	parser = OptionParser()

	parser.add_option('-d', '--dir', dest='dirpath')
	parser.add_option('-t', '--type', dest='filetype', default='xml')

	(option, args) = parser.parse_args()

	if not option.dirpath:
		return parser.error('directory path not given. User --dir="path.to.directory" for file statistics')

	return {'dir': option.dirpath, 'type': option.filetype}


def createFileArray(uInput):
	dirList = listdir(uInput['dir'])
	fList = {}
	for f in dirList:
		if f.endswith(".xml"):
			fList[f] = stat(uInput['dir'] + f).st_size

	return Series(fList)


def main():
	userInput = getInput()
	fileSeries = createFileArray(userInput)
	print fileSeries

	print "_" * 79
	print "Description:\n", fileSeries.describe()

	print "_" * 79
	print "Median File Size: %f" % (fileSeries.median())
	print "Total File Size: %f" % (fileSeries.sum())

	# print userInput['dir'], userInput['type']


if __name__ == '__main__':
	main()
