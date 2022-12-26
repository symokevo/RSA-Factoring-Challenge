#!/usr/bin/python3
import math

def is_prime(num):
    i = 3
    if num % 2 == 0:
        return False
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def factor(num):
    if num % 2 == 0:
        i = 2
        print("{}={}*{}".format(num, int(num/i), i))
    else:
        sq = math.sqrt(num)
        if sq % 1 == 0:
            print("{}={}*{}".format(num, sq, int(num/sq)))
            return
        sq = int(sq) + 1
        for i in range(3, sq, +2):
            if num % i == 0:
                if is_prime(i):
                    print("{}={}*{}".format(num, int(num/i), i))
                    return
