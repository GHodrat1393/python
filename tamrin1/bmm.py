__author__ = ''

def bmm(a,b):
    if a == b:
        return b
    elif a > b:
        if a % b == 0:
            return  b
        else:
            c = a % b
            return bmm(b,c)
    else:
        if b % a == 0:
            return a
        else:
            c = b % a
            return  bmm(a,c)
    return

if __name__ == '__main__'
    yhfcuy
    print bmm(14,5)
    print bmm(8,4)
