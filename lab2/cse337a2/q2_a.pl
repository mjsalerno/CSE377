#!/usr/bin/perl
#q2_a.pl
use strict;
use warnings;

for ( my $i = 1; $i < 33; $i++ ) {
    printf( "%5d %5d %5d\n", "$i", $i * 2, $i * $i );
}
