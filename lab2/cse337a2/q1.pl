#!/usr/bin/perl
#q1.pl
use strict;
use warnings;

print "Enter a string: ";
my $str = <>;

print "How many times do you want to print it? ";
my $n = <>;


for (; $n > 0; $n--) {
	print "$str";
}
