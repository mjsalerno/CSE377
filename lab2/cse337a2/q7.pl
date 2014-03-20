#!/usr/bin/perl
#--------------------
#q7.pl
use strict;
use warnings;

my $fname = $ARGV[0];
my $n     = $ARGV[1];
my $count = 0;
my $group = 1;
my %names;

# for (my $i = 1; $i <= $n; $i++) {
# 	$names{$i} = [];
# }

open FILE, "< $fname";
while ( my $line = <FILE> ) {
    chomp($line);
    if ( $count == $n ) {
        $count = 0;
        $group++;
        $names{$group} = [];
    }
    push( @{ $names{ ($group) } }, $line );
    $count++;
}

for my $key ( keys %names ) {
    my @value = $names{$key};
    print "Group Number: $key\n";

    foreach my $x ( @{ $names{$key} } ) {
        print "$x\n";
    }
    print "\n";
}
