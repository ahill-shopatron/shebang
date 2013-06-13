#!/usr/bin/env python

# Consumes a newline-separated list on standard input, spitting it back out on
# standard output as a comma-separated list instead.
#
# Useful if, say, you have a spreadsheet column in your paste buffer and it
# needs to become an IN clause.

from sys import stdin

def nonewln(s):
	if s.endswith('\n'): s = s[:-1]
	return s

print ','.join(map(nonewln, stdin))
