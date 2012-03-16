# Problem 13
#
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# numbers inproblem13.txt
#
# @date 16/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/
import math
import helper

digits = []
with open("problem13.txt") as file:
    data = file.readlines()
    file.close()

sum = 1
for line in data:
	sum += int(line.strip())
print( str(sum)[0 : 10 ] )
