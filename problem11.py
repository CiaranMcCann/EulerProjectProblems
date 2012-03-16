# Problem 11
#
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
#
# @date 16/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/
import math
import helper

digits = []
with open("problem11.txt") as file:
    data = file.readlines()
    file.close()

for line in data:
	lineOfDigits = []
	for digit in (line.strip()).split(" "):
		lineOfDigits.append(int(digit))
	digits.append(lineOfDigits)


largest = 0
WIDTH = 20
HEIGHT = 20

for y in range(0, HEIGHT):
	for x in range(0,WIDTH):
		
		try:
			horzontail = digits[y][x] * digits[y][x+1] * digits[y][x+2] * digits[y][x+3] 
		except:
			pass

		try:
			vertical = digits[y][x] * digits[y+1][x] * digits[y+2][x] * digits[y+3][x]
		except:
			pass
		
		try:
			diagonalLeft =  digits[y][x] * digits[y+1][x-1] * digits[y+2][x-2] * digits[y+3][x-3]
		except:
			pass
		
		try:
			diagonalRight =  digits[y][x] * digits[y+1][x+1] * digits[y+2][x+2] * digits[y+3][x+3]
		except:
			pass

		if horzontail > largest:
			largest = horzontail
		
		if vertical > largest:
			largest = vertical

		if diagonalLeft > largest:
			largest = diagonalLeft

		if diagonalRight > largest:
			largest = diagonalRight

print(largest)