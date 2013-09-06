#!/usr/bin/env python
#
# Acting as a filter, transmute CSVs with one delimiter to CSVs with another
# delimiter.
#
# TODO: operate on files given on the command line.

import argparse
from sys import stdin, stdout
import csv

aparse = argparse.ArgumentParser()
aparse.add_argument('-i', '--input',
	help='The delimiter used by the input CSV. Defaults to ",".',
	default=',')
aparse.add_argument('-o', '--output',
	help='The delimiter to be used by the output CSV. Defaults to "|".',
	default='|')

args = aparse.parse_args()

csv.writer(stdout, delimiter=args.output).writerows(csv.reader(stdin, delimiter=args.input))
