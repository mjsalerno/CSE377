#!/usr/bin/perl
use strict;
use warnings;

sub corse_title {
    my @c     = @{ $_[0] };
    my $index = $_[1]-1;
    my $cname = $_[2];

    if ( !exists $c[$index]{$cname} ) {
        return "Unknown course";
    }
    else {
        return "$c[$index]{$cname}";
    }
}

my %y1 = ( 114, "Computer Science I" );
my %y2 = ( 220, "Systems-Level Programming" );
my %y3 = ( 320, "Computer Organization and Architecture" );

my @classes = [ \%y1, \%y2, \%y3 ];

print corse_title( @classes, 1, 114 ), "\n";
print corse_title( @classes, 2, "220" ), "\n";
print corse_title( @classes, 3, "320" ), "\n";
print corse_title( @classes, 2, "214" ), "\n";
