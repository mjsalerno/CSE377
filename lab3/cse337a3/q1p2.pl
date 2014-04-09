
#!/usr/bin/perl
####################
#Question 1 part 2
use strict;
use warnings;

print "Enter the regex: ";
my $regex = <>;
chomp($regex);

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
	if ($str =~ m/$regex/) {
		print "$`<$&>$' \n";
	} else {
		print "NO MATCH: $str\n";
	}
}
