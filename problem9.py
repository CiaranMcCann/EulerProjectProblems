# Problem 9
#
#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#
# @date 16/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/


for a in range(1,500):
    for b in range(a+1,500):
        c=1000-a-b
        if a*a+b*b == c*c:
        	print( a * b * c)