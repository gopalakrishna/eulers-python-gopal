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

"""Find the greatest product of five consecutive digits in the 1000-digit number.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""

class Problem8:
    def CalculateProduct(self):
        thousandDigitString = ('73167176531330624919225119674426574742355349194934'
                                '96983520312774506326239578318016984801869478851843'
                                '85861560789112949495459501737958331952853208805511'
                                '12540698747158523863050715693290963295227443043557'
                                '66896648950445244523161731856403098711121722383113'
                                '62229893423380308135336276614282806444486645238749'
                                '30358907296290491560440772390713810515859307960866'
                                '70172427121883998797908792274921901699720888093776'
                                '65727333001053367881220235421809751254540594752243'
                                '52584907711670556013604839586446706324415722155397'
                                '53697817977846174064955149290862569321978468622482'
                                '83972241375657056057490261407972968652414535100474'
                                '82166370484403199890008895243450658541227588666881'
                                '16427171479924442928230863465674813919123162824586'
                                '17866458359124566529476545682848912883142607690042'
                                '24219022671055626321111109370544217506941658960408'
                                '07198403850962455444362981230987879927244284909188'
                                '84580156166097919133875499200524063689912560717606'
                                '05886116467109405077541002256983155200055935729725'
                                '71636269561882670428252483600823257530420752963450')
        largestSubStringIndex = 0
        largestProduct = int(thousandDigitString[0]) * int(thousandDigitString[1]) * int(thousandDigitString[2]) * int(thousandDigitString[3]) * int(thousandDigitString[4])
        currentIndex = 5
        while currentIndex < 1000:
            currentProduct = (int(thousandDigitString[currentIndex]) * int(thousandDigitString[currentIndex + 1]) * 
               int(thousandDigitString[currentIndex + 2]) * int(thousandDigitString[currentIndex + 3]) * 
               int(thousandDigitString[currentIndex + 4])) 
            if (currentProduct > largestProduct):
                largestProduct =  currentProduct
                largestSubStringIndex = currentIndex
            
            if (currentProduct == 0):
                '''start from the highest offset and then count down. Since we require the largest jump'''
                if (int(thousandDigitString[currentIndex + 4]) == 0):
                    currentIndex = (currentIndex + 4) + 1
                    continue
                
                if (int(thousandDigitString[currentIndex + 3]) == 0):
                    currentIndex = (currentIndex + 3) + 1
                    continue                
            
                if (int(thousandDigitString[currentIndex + 2]) == 0):
                    currentIndex = (currentIndex + 2) + 1
                    continue

                if (int(thousandDigitString[currentIndex + 1]) == 0):
                    currentIndex = (currentIndex + 1) + 1
                    continue

                currentIndex = currentIndex + 1
            else:
                currentIndex = currentIndex + 1   
        
        return largestProduct
    
    def __init__(self):
        print('Project Euler: Problem 8: ')
        print('The required largest product is: ' + str(self.CalculateProduct()))
    
res = Problem8()
    
                             