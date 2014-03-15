#!/usr/bin/perl
#q2_b.pl
use strict;
use warnings;

foreach my $i (1..32) {
	printf("%5d %5d %5d\n", "$i", $i * 2, $i * $i);
}