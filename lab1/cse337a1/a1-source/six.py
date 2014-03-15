__author__ = 'michael'
#six
#ask for month and year then find files matching greater than 12000 bytes
#-rw-r--r-- 1 jsmith student 16858 17 Nov 2011 test1


def main():
    minsize = 12000
    filename = raw_input('Enter the file name: ')
    fil = open(filename, 'r')
    month = raw_input('Which month are you interested in? ')
    month = month.capitalize()
    year = input('Which year are you interested in? ')

    for line in fil:
        lst = line.split()
        if int(lst[4]) > minsize and lst[6] == month and int(lst[7]) == year:
            print line,

    fil.close()

main()

