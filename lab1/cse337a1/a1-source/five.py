import math
#five
__author__ = 'michael'

#lst = '230 104 316 110 104 126'


def main():
    lst = raw_input('Enter you course numbers: ')
    l = lst.split()                 #make a list out of the input
    dic = {}

    st = set(l)                     #remove all of the duplicate values by changing it to a set

    for i in st:
        i = int(i)
        i /= 100                    #get the hundreds place
        i = math.floor(i)           #remove decimal
        i *= 100                    #replace the old 10 and 1's place with 0's
        i = int(i)                  #convert to int

        dic[i] = dic.get(i, 0) + 1  #keep count in dict

    for key in dic:
        print str(key) + ' : ' + str(dic[key]) + ' ',


main()
