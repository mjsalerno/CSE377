#!/usr/bin/perl
use strict;
use warnings;

my @strings = ();
my $in;

print "Press ctrl-D to stop entering strings\n";
print "Enter the strings to check\n";

while ( $in = <> ) {
    chomp($in);
    push( @strings, $in );
}

print "\n";

foreach my $str (@strings) {
    if ( $str =~ m/foo/ && $str =~ m/bar/ ) {
        print "$str\n";
    }
    else {
        print "NO MATCH: $str\n";
    }
}
