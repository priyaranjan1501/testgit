import math


def gcd(l):
    vals = l.split(',')
    print(vals)
    l = []
    for ele in vals:
        l.append(int(ele))
    print('Input list is', l)

    # l=[2,4,5,14,13]
    # l=[5,3,5,7,11,2]
    # l=[5,2,3,2,3,3]
    try:
        for i in l:
            if (i == 1 or i == 0):
                raise ValueError("Error:Please don't enter 0 or 1")
    except ValueError as e:
        print(e)
        n = input('Input the numbers separated with comma..Please dont enter 0 or1 ')
        l = str(n)
        gcd(l)
    l1 = []
    lst = l
    # lf=[]
    # setting the counter
    n = 0

    for i in range(len(l)):

        if (len(lst) > 0):
            # print(i)
            x = lst[0]
            # print(x)
            l1.append(x)
            # lf.append(x)
            lst.remove(x)
            # Incrementing the counter
            n = n + 1
            # print('n check')

        if (len(lst) > 0):
            print("x",x)
            l2 = list(gcd1(x, l))

            if (len(l2) > 0):
                for ele in l2:

                    lst.remove(ele)

                else:

                    #print("l1before",l1)
                    l1.extend(l2)
                    #print("l1",l1)

            else:

                print(l1)

            l1.clear()
    else:
        print(l1)

    print('No.of good arrays will be', n)


def gcd1(x, l):
    l1 = []
    if (len(l) > 0):
        for j in l:
            g = math.gcd(x, j)
            if g > 1:
                l1.append(j)
    # print('gcd1 l1',l1)
    #print(l1)
    return l1


n = input('Input the numbers separated with comma,lik 3,4,5.Please dont enter 0 or1  ')
l = str(n)
gcd(l)
