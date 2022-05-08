#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2020 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import cython
from libc.math cimport sqrt
from libc.stdlib cimport malloc, free


@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline double sum(list y):
    cdef int N, i 
    N = len(y)
    cdef double x = y[0]
    for i in xrange(1,N):
        x += y[i]
    return x


cpdef double average(list x, bint bessel=False):
    '''
    Args:
      x: iterable with len

      oneless: (default ``False``) reduces the length of the array for the
                division.

    Returns:
      A float with the average of the elements of x
    '''
    cdef int N = len(x)
    return sum(x) / (N - bessel)


cpdef list variance(x, avgx=None):
    '''
    Args:
      x: iterable with len

    Returns:
      A list with the variance for each element of x
    '''
    if avgx is None:
        avgx = average(x)
    return [pow(y - avgx, 2.0) for y in x]


cpdef double standarddev(x, avgx=None, bint bessel=False):
    '''
    Args:
      x: iterable with len

      bessel: (default ``False``) to be passed to the average to divide by
      ``N - 1`` (Bessel's correction)

    Returns:
      A float with the standard deviation of the elements of x
    '''
    return sqrt(average(variance(x, avgx), bessel=bessel))
