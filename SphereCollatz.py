#!/usr/bin/env python3

# ------------------------------
# SphereCollatz.py
# Fatimah Zohra
# ------------------------------

# -------
# imports
# -------

import sys

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0 and i < 1000000
    assert j > 0 and j < 1000000

    if i > j:
        temp = i
        i = j
        j = temp

    # simple lazy cache
    cache = {}

    m = 1  #initialize a max variable

    for n in range(i, j+1):
        c = 1 #initialize a count variable
        orig = n
        while n != 1:
            if n in cache:
                c = cache[n] + c - 1
                n = 1
            else:
                if n % 2 == 0:
                    n = n / 2
                else:
                    n = 3 * n + 1
                c += 1
        cache[orig] = c
        m = max(c, m)
    return m


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)

# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)

