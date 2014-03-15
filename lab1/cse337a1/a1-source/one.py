__author__ = 'michael'
#one


def main():
    """print the second largest number in a set"""

    s = set()

    while True:
        n = input('Enter a number: ')
        if n == -99:
            break

        s.add(n)

    l = list(s)

    if len(l) < 2:
        print 'sorry but the list is too small'
        exit(1)

    l.sort()
    print 'The second largest number is', l[-2]


main()
