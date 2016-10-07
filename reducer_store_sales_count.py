#!/usr/bin/env python

import sys

def reducer():

    salesTotal = 0
    oldKey = None

    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        if not data or len(data) != 2:
            continue

        thisKey, thisSale = data

        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, salesTotal)
            salesTotel = 0

        oldKey = thisKey
        salesTotal += float(thisSale)
        
    if oldKey != None:
        print "{0}\t{1}".format(oldKey, salesTotal)
        

if __name__ == "__main__":
    reducer()

#Self-test
#HadoopMR$ cat purchase_self_testfile | ./mapper_store_sales_count.py | sort | ./reducer_store_sales_count.py
