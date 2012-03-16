# Problem 16
#
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
#
# @date 16/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/
from decimal import *
import math
digits = str(Decimal( math.pow(2,1000) ))
answer = 0
for digit in digits:
	answer += int(digit)

print(answer)