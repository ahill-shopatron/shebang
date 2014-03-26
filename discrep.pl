#!/usr/bin/env perl

use strict;
use warnings;

my $site = undef;
my $expected = undef;
my $actual = undef;
my $table = undef;

while (<>) {
	if (/^Site (\D+?) \d/) {
		$site = $1;
		$expected = undef;
		$actual = undef;
		$table = undef;
	} elsif (/^Found (\d+) records in table (.*)$/) {
		$expected = $1;
		$table = $2;
		$actual = undef;
	} elsif (/^Published (\d+) records to/) {
		$actual = $1;
	}

	if (defined($expected) && defined($actual) && $expected != $actual) {
		print "$table for $site: found $expected, published $actual\n";
	}
}
