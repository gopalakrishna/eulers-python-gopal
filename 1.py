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

"""Problem 1: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import Common

class First:
    def Sum(self, upto):
        firstNumber = 3
        secondNumber = 5
        """sum = sum of mutliples of 3 + sum of multiples of 5 - sum of multiples of 15(LCM of 3 and 5)"""
        return int(Common.EulerCommon.SumSeries(firstNumber, upto) + Common.EulerCommon.SumSeries(secondNumber, upto) - Common.EulerCommon.SumSeries(Common.EulerCommon.findLCM(firstNumber, secondNumber), upto))
    
    def __init__(self):
        print('Project Euler: Problem 1: ')
        upto = int(input('Enter the number below which you want the sum:'))
        print('The sum is: ' + str(self.Sum(upto-1)))

run=First()