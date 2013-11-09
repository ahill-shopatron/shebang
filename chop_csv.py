#!/usr/bin/env python
#
# Acting as a filter, keeps only the first n lines of an input CSV

import csv

def chop(src, n, delim=','):
	for row in csv.reader(src, delimiter=delim):
		yield row[0:n]

if __name__ == '__main__':
	import argparse
	from sys import stdin, stdout

	aparse = argparse.ArgumentParser()
	aparse.add_argument('-d', '--delimiter',
			help='The delimiter used by the CSV. Defaults to ",".',
			default=',')
	aparse.add_argument('n',
			type=int,
			help='The number of leading cells to keep.')

	args = aparse.parse_args()

	csv.writer(stdout, delimiter=args.delimiter).writerows(chop(stdin, args.n, delim=args.delimiter))
