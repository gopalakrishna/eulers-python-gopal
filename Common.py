
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

"""This file contains the set of functions that are used across solutions.
"""
import math

class EulerCommon:
    @staticmethod
    def SumSeries(multiplesOf, sumUpto):
        n = int(sumUpto / multiplesOf)
        return multiplesOf * (n * (n + 1)/2)
    
    @staticmethod
    def findLCM(firstNumber, secondNumber):
        if firstNumber <= 0 or secondNumber <= 0 :
            return 0
        return (firstNumber * secondNumber) / EulerCommon.findGCD(firstNumber, secondNumber)
    
    @staticmethod
    def findGCD(numberOne, numberTwo):
        firstNumber = numberOne
        secondNumber = numberTwo
        if firstNumber <= 0 or secondNumber <= 0 :
            return 0
        while secondNumber != 0 :
            remainder = firstNumber % secondNumber
            firstNumber = secondNumber
            secondNumber = remainder
        return firstNumber
    
    @staticmethod
    def CheckPrime(number):
        if number<= 2:
            return True
        squareRoot = math.sqrt(number)
        
        i = 2
        while i <= squareRoot:
            if number % i == 0:
                return False
            else:
                i +=1
        
        return True
            
