#!/usr/bin/env python3
"""From CodeAbbey
Here is the link: http://www.codeabbey.com/index/task_view/sort-with-indexes
But it's String variant
"""
array = []
array.append("Hello")
array.append("World")
array.append("and")
array.append("everyone")

for i in list(range(len(array))):
	index = array.index(array[i])
	print(index)
