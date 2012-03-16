# Some helper python functions, that I use alot in solving problems
# 
# @date 16/03/2012 
# @author Ciarán McCann
# @website http://ciaranmccann.me/
#

def chunk(collection, chuckSize):
    return [collection[i:i+chuckSize] for i in range(0, len(collection), chuckSize)]

def printItems(n1="",n2="",n3="",n4="",n5=""):
	print("N1 = " + str(n1) + "  N2 = " + str(n2) + "  N3 = " + str(n3) + "  N4 = " + str(n4) + "  N5 = " + str(n5))

def printGridArray(array,width = 10):
	rows = chunk(array,width)
	print(" ")
	for row in rows:
		print(row)
	print(" ")