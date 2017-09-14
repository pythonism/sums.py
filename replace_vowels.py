#!/usr/bin/env python3
def replaceStr(str,c,c2):
	i = 0
	d = 0
	n_str = ""
	
	while i < len(str):
		if str[i] == c[d]:
			n_str += c2
		else:
			n_str += str[i]
		i+=1
	return n_str


	
	

def reStr(str,c,c2):
	i = 0
	strs = str
	while i < len(c):
		strs = replaceStr(strs,c[i],"")
		i+=1
	return strs
	

Str = "Hey You"

p = reStr(Str,"eou","")

print(p)
