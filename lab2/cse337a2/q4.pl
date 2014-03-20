#!/usr/bin/perl
#q4.pl
use strict;
use warnings;

use constant PI => 3.141593;

#area = Pi * r *r
#circ = Pi * d
sub circle_stats {
    my $r = $_[0];
    my $a = PI * $r * $r;
    my $d = 2 * $r;
    my $c = PI * $d;

    return wantarray ? ( $a, $d, $c ) : $a;
}

print "enter a radius: ";
my $n = <>;

my $a = circle_stats($n);
my @l = circle_stats($n);

print "just scaler: $a\n";
print "a list: @l\n";
