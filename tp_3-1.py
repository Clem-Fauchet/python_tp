# -*- coding: utf-8 -*-
#!/usr/bin/python

quantity = input("Saisir une quantité ")
q = int(quantity)
price = input("Saisir un prix ")
p = float(price)

if(q <= 0 or p <= 0):
  print("Veuillez saisir des données correctes")
  
else:
  totalPrice = round(q * (p * 1.2), 2)

  if (totalPrice > 200):
    remisePrice = float(totalPrice * 0.05)
    newPrice = round(totalPrice - remisePrice, 2)
    print(newPrice)
  
  else :
    print(totalPrice)

