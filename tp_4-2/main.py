# -*- coding: utf-8 -*-
#!/usr/bin/python

import calcul
import inputFile

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

print(inputFile.userInput("le nombre de produits à acheter", nbP)) #module input


for i in range (0, nbP): #loop pour each product

  print(inputFile.userInput("l'id du produit à ajouter au panier", pdtCh)) #module input

  try:
    print(table[pdtCh - 1 ]) #table index start with 0

    print(inputFile.userInput("une quantité", q))


    priceProductChosen = dProduct[pdtCh].get('price')
    prPdtCh = float(priceProductChosen)

    priceHT = calcul.calcPriceHT(q, prPdtCh) #module calcul

    totalPaid += priceHT #increment total each time


    def updateDictonary():

      itemSelected = dProduct[pdtCh] 
      quantitySelected = quantity.split(':') 
      quantitySelected = ''.join(quantitySelected) 

      itemSelected['quantity'] = abs(int(quantitySelected)) 
      qItem = itemSelected['quantity']
      return qItem 

      itemSelected['totalHT'] = priceHT
      totalItem = itemSelected['totalHT']
      return totalItem



  except IndexError: #si id out of range
    print("Veuillez saisir un id valide. ")
    break


  except ValueError: #si quantité float number
    print("Veuillez saisir une quantité valide. ")
    break


newTable = PrettyTable(['Name', 'Price', 'Quantity','Total HT'])


for key,value in dProduct.items():

  if 'quantity' in value:
    newTable.add_row([value['name'], value['price'], value['quantity'], value['totalHT']])
   
  else:
    None
 
else: 
  None


print(newTable)


print('Total HT : '+ str(totalPaid) + '€') #total all products


if totalPaid < 200: 
  
  priceTTC = calcul.calcPriceTTC(totalPaid) #module calcul

else:

  remisePrice = calcul.calcRemise(totalPaid) #module calcul

  priceHTAfter = calcul.calcPriceHTAfter(totalPaid, remisePrice) #module calcul

  priceTTC = calcul.calcPriceTTC(priceHTAfter) #module calcul