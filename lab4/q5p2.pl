#!/bin/perl

use strict;
use warnings;

my @files = `ls`;
@files = grep(!/\.html$/, @files);

my @count;
my $countstr;

foreach my $f (@files) {
	chomp($f);

	$countstr = `wc $f`;
	chomp($countstr);

	@count = split(" ", $countstr);

	if ($count[0] > 19) {
		print "$f has $count[0] lines\n"
	}
}