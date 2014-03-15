__author__ = 'michael'
#seven

def printprime(lst):
    if len(lst) == 0:
        return
    print lst[0],
    printprime(filter(lambda x: x % lst[0] != 0, lst))


def main():
    #lst = [randrange(1, 10) for _ in range(10)]
    lst = range(2, 1001)
    print filter(lambda x: x % lst[0] != 0, lst)
    printprime(lst)

main()
