#! /usr/bin/python

""" Download Accelerator

	A Python utility to download files by parsing a csv file
	It uses `aria2` command line download accelerator utility
	For more information on `aria2` refer: http://aria2.sourceforge.net/
"""

__author__ = "Shreyas"
__email__ = "shreyas@ischool.berkeley.edu"
__python_version = "Python 2.7.3 -- EPD 7.3-2 (32-bit)"

from optparse import OptionParser
from csv import reader
import subprocess
from time import time
import sys


def getInput():
	""" Command Line Input Parsing

		Parse the user input
	"""
	parser = OptionParser()
	parser.add_option('-i', '--input', dest='filepath')
	parser.add_option('-f', '--format', dest='dnldFormat', default='djvu')
	parser.add_option('-u', '--utility', dest='utility', default='aria2')
	(option, args) = parser.parse_args()

	if not option.filepath:
		return parser.error('CSV file path not given, use --input="path.to.csv.file.for.download"')

	return {'src': option.filepath, 'format': option.dnldFormat, 'utility': option.utility}


def getDnldList(src, format):
	""" Create Downloadable list

		Parse a CSV file to get book identifiers to create a list of
		book-ids to be downloaded
	"""
	print "Parsing %s to get download urls " % (src)
	fObj = open(src, 'rb')
	f = reader(fObj)
	# dList = [''.join(row) for row in f]
	dList = []
	#http://archive.org/stream/cawcaworchronicl00rmrmiala/cawcaworchronicl00rmrmiala.djvu
	urlPrefix = 'http://www.archive.org/download/'
	rowNum = 0

	for row in f:
		if rowNum > 0:
			#Skip the first row for headers
			fileId = ''.join(row)
			url = urlPrefix + fileId + '/' + fileId + '_' + format + '.xml'
			dList.append(url)
		else:
			rowNum += 1

	fObj.close()
	return dList


def initDnld(dList, util):
	if util == 'aria2':
		# subprocess.call("aria2c" ' '.join)
		# args = ' '.join(item for item in dList)
		# subprocess.call(["wget", "-O", args ])


		# creating a text file for aria because it can automatically parse
		# for urls in a text file and download them
		fObj = open("downloads/aria2/_downloadlist.txt", "w")
		fObj.writelines("%s\n" % (item) for item in dList)
		fObj.close()

		#initiate download timestamp
		cmd = 'aria2c -j5 -idownloads/aria2/_downloadlist.txt -x2 --dir=downloads/aria2'

	elif util == 'curl':
		cmd = ''

	elif util == 'wget':
		cmd = ''
	else:
		print "Incorrect Utility Input. Choose [aria2c]/[wget]/[curl]"
		return

	print "Starting Downloads"
	t0 = time()
	# p = subprocess.Popen(["aria2c", "-j5", "-idownloads/aria2/_downloadlist.txt", "-x2", "--dir=downloads/aria2"], stdout=subprocess.PIPE)
	p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
	while True:
		out = p.stderr.read(1)

		if out == '' and p.poll is not None:
			break

		if out != '':
			sys.stdout.write(out)
			sys.stdout.flush()
	# output, err = p.communicate()

	# print "**Downloading Complete ** \n", output

	print "\n\n=========> Downloaded in : %f s\n\n" % (time()-t0)
	print "Back in Python"



def main():
	userInput = getInput()
	dnldList = getDnldList(userInput['src'], userInput['format'])
	initDnld(dnldList, userInput['utility'])
	# print dnldList



if __name__ == '__main__':
	main()
