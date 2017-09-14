#!/usr/bin/env python2

def reverse(text):
  array = []
  count = 1

  for i in list(range(len(text))):
    array.append(text[len(text)-count])
    count+=1
  array = ''.join(array)
  return array

print reverse('Hello World!')
