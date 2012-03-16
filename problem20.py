# Problem 20
#
# n! means n  (n  1)  ...  3  2  1
#
# For example, 10! = 10  9  ...  3  2  1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#
# @date 16/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/

num = n = 100
for i in range(1,n):
	num *= n-i

sum = 0
for digit in str(num):
	sum += int(digit)

print(sum)