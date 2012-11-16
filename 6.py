""" This file is part of the set of solutions to Project Euler
 # Copyright (C) 2011 Gopalakrishna Bhat A <gopalakbhat@gmail.com>
 #
 # This library is free software; you can redistribute it and/or
 # modify it under the terms of the GNU Library General Public
 # License as published by the Free Software Foundation; either
 # version 2 of the License, or (at your option) any later version.
 #
 # This library is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 # Library General Public License for more details.
 #
 # You should have received a copy of the GNU Library General Public License
 # along with this library; see the file COPYING.LIB.  If not, write to
 # the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 # Boston, MA 02110-1301, USA.
"""

"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

class Problem6:
    def findDifference(self, numberUpto):
        """ We use the the formula that sum of natural numbers upto n is given by n*(n+1)/2
        also sum of squares of numbers is given by n*(n+1)*(2n+1)/6
        """
        n = numberUpto
        result = (n * (n + 1) * ((3 * n* n) - n - 2)) / 12
        return int(result)
    def __init__(self):
        print('Project Euler: Problem 6: ')
        inputNumber = int(input('Enter the number until which the difference should be calculated:'))
        print('The required number is: ' + str(self.findDifference(inputNumber)))
        
run = Problem6()