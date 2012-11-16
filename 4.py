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

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

class Problem4:
    def LargestPalindromeProduct(self):
        multiplicand = 990 #990 is the largest 3-digit multiple of 11 and then count downwards is steps of 11 
        """We use the property that any even digited palindrome will be a multiple of 11"""   
        maxPal = 0
        while (multiplicand >= 100):
            multiplier = 999  # We start with the largest 3-digit number possible and count downwards
            while (multiplier >= multiplicand):
                product = multiplicand * multiplier
                if (str(product) == ''.join(reversed(str(product)))):
                    if (product > maxPal): 
                        maxPal = product
                multiplier = multiplier - 1
            multiplicand = multiplicand - 11 
        return maxPal
    
    def __init__(self):
        print('Project Euler: Problem 4: ')
        print('The largest palindrome of product of two 3-digit numbers is: ' + str(self.LargestPalindromeProduct()))
        
run = Problem4()
                
                
                
                