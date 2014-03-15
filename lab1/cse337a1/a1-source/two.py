import sys
#two
__author__ = 'michael'

msg = \
    """fjxdfkb qebob'p kl zlrkqofbp fq fpk'q exoa ql al klqefkd ql hfii lo afb clo
xka kl obifdflk qll fjxdfkb xii qeb mblmib ifsfkd ifcb fk mbxzb vlr jxv pxv
qexq F'j x aobxjbo yrq F'j klq qeb lkiv lkb f elmb pljbaxv vlr'ii glfk rp
xka qeb tloia tfii yb xp lkb
"""


def main():

    print msg

    for c in msg:
        c = ord(c)
        if (97 <= c) and (c <= 122):
            c += 3
            if c > 122:
                c = (c-122) + 96

        elif (65 <= c) and (c <= 90):
            c += 3
            if c > 90:
                c = (c - 90) + 64

        sys.stdout.write(str(chr(c)))
main()
