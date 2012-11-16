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

""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

class Problem9:
    def __init__(self):
        print('Project Euler: Problem 9: ')
        print('The required product is: ' + str(self.CalculateProduct()))
    
    def CalculateProduct(self):
        """ To calculate a*b*c we use the property that (a + b + c) ^ 2 = a^2 +b^2 + c^2 + 2*a*b +2*b*c + 2*a*c
            Which when simplified using a^2 + b^2 = c^2 and a+b+c=1000 we get
            (500 - c) = (a * b) / 1000
        """
        a = 1
        b =  500 #since c must be less than 500 and b < c
        c = 0
        loopFlag = True
        while loopFlag:
            while a < b:
                if (((a * b) % 1000) == 0):
                    print("loop" + str(a) + " " + str(b) + " "+ str(c))
                    c = 500 - ((a * b) / 1000)
                    if (a + b + c == 1000):
                        break
                a = a + 1
                b = b - 1
            
            if (a + b + c == 1000):
                return a * b * c
            else:
                print(str(a) + " " + str(b) + " "+ str(c))
                return 0

res = Problem9()
            