#!/usr/bin/env python
#
# Acting as a filter, repair one very specific kind of CSV mangling.

import sys
import csv

def demunge(line):
	if len(line) == 1:
		return csv.reader(line, delimiter='|').next()
	else:
		return line

reader = csv.reader(sys.stdin, delimiter='|')
writer = csv.writer(sys.stdout, delimiter='|')

writer.writerows(map(demunge, reader))
