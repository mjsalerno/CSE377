#!/usr/bin/perl
#q6.pl
use strict;
use warnings;

print "Enter the name of the file: ";
my $fname = <>;
chomp($fname);

open FILE, "< $fname";

while ( my $line = <FILE> ) {
    chomp($line);

    $line =~ s/^\d+\s//;

    print "$line\n";
}

close(FILE);
