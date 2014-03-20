#!/usr/bin/perl
#--------------------
#q5.pl
use strict;
use warnings;

my %map;

while (<>) {
    chomp;
    my @line = split( ' ', $_ );

    foreach my $word (@line) {

        if ( !exists $map{$word} ) {
            $map{$word} = 0;
        }

        $map{$word} = $map{$word} + 1;
    }
}

print "\n--------------------\n";
print "$_ $map{$_}\n" for ( keys %map );
print "\n";
