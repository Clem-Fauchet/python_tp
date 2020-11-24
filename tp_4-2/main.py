# -*- coding: utf-8 -*-
#!/usr/bin/python

import calcul
import input

from prettytable import PrettyTable


dProduct = {
            1: {'name':'Banane', 'price': 4}, 
            2: {'name':'Pomme', 'price': 2}, 
            3: {'name':'Orange', 'price': 1.5},
            4: {'name':'Poire', 'price': 3}
          }


table = PrettyTable(['Id', 'Name', 'Price']) # first table dictionnary

for (key,value) in dProduct.items():
   table.add_row([key, value['name'], value['price']])


print(table)

totalPaid = 0.0 #init total

print(input.userInput("le nombre de produits à acheter", nbP))



for i in range (0, nbP): #loop pour each product

  print(input.userInput("l'id du produit à ajouter au panier", pdtCh))

  try:
    print(table[pdtCh - 1 ]) #table index start with 0

    print(input.userInput("une quantité", q))


    priceProductChosen = dProduct[pdtCh].get('price')
    prPdtCh = float(priceProductChosen)

    priceHT = calcul.calcPriceHT(q, prPdtCh)
    
    totalPaid += priceHT #increment total each time



  except IndexError: #si id out of range
    print("Veuillez saisir un id valide. ")
    break


  except ValueError: #si quantité float number
    print("Veuillez saisir une quantité valide. ")
    break