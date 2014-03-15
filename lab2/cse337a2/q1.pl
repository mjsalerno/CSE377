#!/usr/bin/perl
use strict;
use warnings;

print "Enter a string: ";
my $str = <>;

print "How many times do you want to print it? ";
my $n = <>;


for (; $n > 0; $n--) {
	print "$str";
}
