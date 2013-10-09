#!/usr/bin/env python
#
# Acting as a filter, keeps only the first n lines of an input CSV

import argparse
from sys import stdin, stdout
import csv

aparse = argparse.ArgumentParser()
aparse.add_argument('-d', '--delimiter',
		help='The delimiter used by the CSV. Defaults to ",".',
		default=',')
aparse.add_argument('n',
		type=int,
		help='The number of leading cells to keep.')

args = aparse.parse_args()

csv.writer(stdout, delimiter=args.delimiter).writerows(
	row[0:args.n] for row in csv.reader(stdin, delimiter=args.delimiter)
)
