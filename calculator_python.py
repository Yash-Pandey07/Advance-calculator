# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:12:06 2020

@author: DELL
"""

import re
print("********WELCOME **********")
print("Type quit to exit")
previous =0
run=True

def performMath():
	global run
	global previous
	equation=""
	if previous==0:
		equation=input("Enter equation: ")
	else:
		equation=input(str(previous))
		
	if equation=='quit':
		print("Good bye ,Thanks for using it")
		run=False
	else:
		equation=re.sub('[a-zA-Z,.:()" "]','',equation)
		
		if previous==0:
			previous=eval(equation)
		else:
			previous=eval(str(previous)+equation)

while run:
	performMath()