
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter Number: ").strip())

    arr = list(map(int, input("Enter array: ").rstrip().split()))

    for i in range(0,n):
        i+=1
        rev= arr[-i]
        print(rev, end=" ")
