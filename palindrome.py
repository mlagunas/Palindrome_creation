# -*- coding: utf-8 -*-

# Author; Manuel Lagunas
# 3/9/2016
# Readable code implementing huffman compression/decompression
import sys
import numpy


def usage():
    print "USAGE"
    print "python palindrome.py text"
    print "	 \"text\" is the list of characters we will transform into a palindrome"

# This functions return true if the input is a palindrome, false otherwise


def isPalindrome(input):
    return str(input) == str(input)[::-1]

# The function fills an matrix with the minimum edit distance to transform a string x to y.
# Each position in the matrix precomputes the minimum edit distance for
# the substring x_i y_j


def edDistDp(x,	y):
    D = numpy.zeros((len(x) + 1, len(y) + 1), dtype=int)
    # if x is empty the minimum distance must be the lenght of y
    D[0, 1:] = range(1, len(y) + 1)
    # if y is empty the minimum distance must be the lenght of x
    D[1:, 0] = range(1, len(x) + 1)
    for i in xrange(1,	len(x) + 1):
        for j in xrange(1,	len(y) + 1):
            delt = 1 if x[i - 1] != y[j - 1] else 0
            insert = D[i][j - 1]
            remove = D[i - 1][j]
            replace = D[i - 1][j - 1]
            D[i, j] = min(replace + delt,
                          remove + 1,
                          insert + 1)
    return D

# This function reads back the DP matrix with the minimum edit distances,
# storing the operation used.


def backtrace(a, b, D):
    i, j = len(a), len(b)
    result = ""
    indices = []
    while(not (i == 0 and j == 0)):
        indices.append([i, j, D[i, j]])
        # Get edit distance for the substrings x_i y_j
        last = D[i][j]
        # Get the operation that returns the minimum edit distance
        insert = D[i][j - 1]
        remove = D[i - 1][j]
        replace = D[i - 1][j - 1]
        aux = min(insert,
                  remove,
                  replace)
        if(aux == last):  # Characters are the same
            i, j = i - 1, j - 1
            result += ' '
        elif(i != 0 and aux == remove):
            i, j = i - 1, j
            result += 'D'
        elif(j != 0 and aux == insert):
            i, j = i, j - 1
            result += 'A'
        elif(i != 0 and j != 0 and aux == replace):
            i, j = i - 1, j - 1
            result += 'S'
    return result[::-1], indices

# This function creates all the possible substrings from a string and
# checks their minimum edit distance storing the minimum value together
# with the substrings


def getSmallestED(entrada):
    mined = -1
    minD = None
    mina = ''
    minb = ''
    for i in range(len(entrada)):
        # Slice string
        a = entrada[:i]
        b = entrada[i:]
        D = edDistDp(a, b[::-1])
        # Check if it is the minimum value
        if D[len(a)][len(b)] < mined or mined == -1:
            mined = D[len(a)][len(b)]
            mind = D
            mina = a
            minb = b
    return mina, minb, mind

# The function reads back the string returned by the backtrace of the DP
# matrix and make the modifications to the characters that need it
# returning the operations that it has done together with the resulting
# word and a boolean that will show if it is or not a palindrome


def makePalindrome(entrada):
    a, br, D = getSmallestED(entrada)
    b = br[::-1]
    D = edDistDp(a, b)
    offset = 0
    S, indices = backtrace(a, b, D)
    # There are some cases where the last Addition is not necessary, Thats why
    # it just copy the last character of the first substring (the first of the
    # second substring) when it can be used as a pivot.
    if (S[-1] == 'A'):
        offset = 1
    print "Numero minimo: " + str(D[len(D) - 1][len(D[0]) - 1] - offset)
    print "Cadena original: " + entrada
    a = list(a)
    x, i, j = 0, 0, 0
    # Build the new string by reading the operations obtained thanks to the DP
    # matrix with the minimum edit distance
    while x < (len(S) - offset):
        op = S[x]
        if op == 'S':
            a[i] = b[j]
            print "Cambiar pos " + str(i + 1) + " por " + b[j] + ": " + "".join(a) + br
            i += 1
            j += 1
        elif op == 'D':
            a[i] = ''
            print "Borrar posición " + str(i + 1) + ": " + "".join(a) + br
            i += 1
        elif op == 'A':
            a.insert(i, b[j])
            print "Añadir " + b[j] + " en pos " + str(i) + ": " + "".join(a) + br
            j += 1
            i += 1
        else:
            i += 1
            j += 1
        x += 1
    a = "".join(a)
    # print a + br
    # print "es Palindromo?", isPalindrome(a + br)

if len(sys.argv) == 2:
    text = sys.argv[1]
    makePalindrome(text)
else:
    usage()
