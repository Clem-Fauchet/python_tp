# -*- coding: utf-8 -*-
#!/usr/bin/python

l1=list(range(4))
print("l1=",l1)
l2=list(range(4, 8))
print("l2=",l2)
l3=list(range(2, 9, 2))
print("l3=",l3)
print(2 in l1, 8 in l2, 6 in l3)


for i in range(len(l3)):
  print(i,l3[i],sep="-",end="")


d1 = {'Pierre':17, 'Paul':15,'Jacques':16}
print(d1)
print(d1.items())
print(len(d1))

print(d1['Paul'])
print(d1.get('Paul'))