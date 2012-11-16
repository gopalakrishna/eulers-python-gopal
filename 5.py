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
import Common

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

class Problem5:
    def MinNumber(self, numberBelow):
        count = 1
        lcm = count
        while (count <= numberBelow):
            lcm = Common.EulerCommon.findLCM(lcm, count)
            count = count + 1
        
        return lcm 
    
    def __init__(self):
        print('Project Euler: Problem 5: ')
        inputNumber = int(input('Enter the number until which the number should be eenly divisible:'))
        print('The minumum evenly divisible number is: ' + str(self.MinNumber(inputNumber)))
        
run = Problem5()