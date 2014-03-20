#!/usr/bin/perl
#q8.pl
use strict;
use warnings;

sub corse_title {
    my @c     = @{ $_[0] };
    my $index = $_[1] - 1;
    my $cname = $_[2];

    if ( !exists $c[$index]{$cname} ) {
        return "Unknown course";
    }
    else {
        return "$c[$index]{$cname}";
    }
}

my %y1 = (
    110, "Introduction to Computer Science",
    114, "Computer Science I",
    130, "Introduction to Programmingin C"
);
my %y2 = (
    214, "Computer Science II", 219, "Computer Science III",
    220, "Systems-Level Programming"
);
my %y3 = (
    303, "Introduction to the Theory of Computation",
    306, "Operating Systems",
    320, "Computer Organization and Architecture"
);

my @classes = [ \%y1, \%y2, \%y3 ];

print corse_title( @classes, 1, 114 ), "\n";
print corse_title( @classes, 2, 220 ), "\n";
print corse_title( @classes, 3, 320 ), "\n";
print corse_title( @classes, 2, 214 ), "\n";
print corse_title( @classes, 3, 306 ), "\n";
print corse_title( @classes, 2, 306 ), "\n";
