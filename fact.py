#!/usr/bin/python3
import math

def fact(num):
    if num % 2 == 0:
        i = 2
        print("{}={}*{}".format(num, int(num//i), i))
    else:
        sq = int(math.sqrt(num)) + 1
        for i in range(3, sq, +2):
            if num % i == 0:
                print("{}={}*{}".format(num, int(num//i), i))
                return
            if num % (sq + i) == 0:
                print("{}={}*{}".format(num, sq + i, int(num//(sq + i))))
                return
            if num % (sq - i) == 0:
                print("{}={}*{}".format(num, sq - 1, int(num//(sq - i))))
                return
