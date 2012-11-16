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
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import Common

class Problem7:
    """ We will be using the property described at http://www.physicsforums.com/archive/index.php/t-96187.html
    to determine if a number is prime or not
    """
    addTwo = True  #boolean
    
    def calculateNthPrimeNumber(self, n):
        count = 1
        currentPrime = 2
        while (count < n):
            currentPrime = self.NextPrimeNumber(currentPrime)
            count = count + 1
        return currentPrime
        
    def NextPrimeNumber(self, currentPrimeNumber):
        if currentPrimeNumber == 2:
            return 3
        
        if currentPrimeNumber == 3:
            return 5
        
        nextPrime = currentPrimeNumber
        
        isNewNumberPrime = False
        
        while not isNewNumberPrime:
            if self.addTwo == True:
                nextPrime += 2
                self.addTwo = False
            else:
                nextPrime += 4 
                self.addTwo = True
                
            isNewNumberPrime = Common.EulerCommon.CheckPrime(nextPrime)
            
        return nextPrime
    
    def __init__(self):
        print('Project Euler: Problem 7: ')
        inputNumber = int(input('Enter the count of the prime number wanted:'))
        print('The required number is: ' + str(self.calculateNthPrimeNumber(inputNumber)))
        
res = Problem7()