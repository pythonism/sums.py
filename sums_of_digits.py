#!/usr/bin/env python3
"""From CodeAbbey
Here is the link: http://www.codeabbey.com/index/task_view/sum-of-digits
"""

def fix(a,b,c):
	d = a*b+c
	array = list(map(int, str(d)))
	return sum(array)

print(fix(10,10,10))
print(fix(50,20,50))
