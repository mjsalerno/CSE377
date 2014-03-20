#!/usr/bin/perl
#q3.pl
use strict;
use warnings;

print "How many lines: ";
my $n = <>;

my @lines;

for ( my $i = 0; $i < $n; $i++ ) {
    print "Enter a line: ";
    my $str = <>;
    chomp($str);
    push( @lines, $str );
}

do {

    my $val = pop(@lines);
    print "$val\n";
    $n--;

} until ( $n == 0 );
