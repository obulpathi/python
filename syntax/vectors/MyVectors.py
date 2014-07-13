#!/usr/bin/env python

import numpy

alg = numpy.linalg
u = numpy.array(1, 2, 3)
G = numpy.array(1, 2, 3, 4, 5, 6, 7, 8, 9)
G.size = (3, 3)

v = dot(G, u)
print v
