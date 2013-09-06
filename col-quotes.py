#!/usr/bin/env python

# Consumes a newline-separated list on standard input, spitting it back out on
# standard output with each line surrounded by single quotes.
#
# Useful if you've got a column from a spreadsheet in the paste buffer, and need
# to quote it for some reason.

from sys import stdin

def quote(s):
	if s.endswith('\n'): s = s[:-1]
	return "'"+s+"'"

for ln in (quote(l) for l in stdin):
	print ln
