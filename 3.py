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

"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import Common

class Problem3:
    """ We will be using the property described at http://www.physicsforums.com/archive/index.php/t-96187.html
    to determine if a number is prime or not
    """
    addTwo = True  #boolean
    
    def LargestPrime(self, number):
        currentPrimeNumber = 2
        largestPrimeFactor = currentPrimeNumber
        
        while number != 1 :
            if number % currentPrimeNumber == 0 :
                largestPrimeFactor = currentPrimeNumber
                number /= currentPrimeNumber
            else:
                currentPrimeNumber = self.NextPrimeNumber(currentPrimeNumber)
                
        return largestPrimeFactor
            
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
        print('Project Euler: Problem 3: ')
        inputNumber = int(input('Enter the number for which the largest prime factor has to be found:'))
        print('The largest pime factor is: ' + str(self.LargestPrime(inputNumber)))
        
run = Problem3()
                
                
