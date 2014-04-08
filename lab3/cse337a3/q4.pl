#!/usr/bin/perl
use strict;
use warnings;

print "Enter a string: ";
my $string1 = <>;
chomp($string1);

$string1 = $string1 =~ s/\D//rg;
print "new string: $string1\n";

my $string2 = reverse $string1;

if ($string1 eq $string2) {
	print "$string1 is a palindrome\n";
} else {
	print "$string1 is NOT a palindrome\n";
}


