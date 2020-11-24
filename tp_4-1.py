# -*- coding: utf-8 -*-
#!/usr/bin/python

from prettytable import PrettyTable


dProduct = {
            1: {'name':'Banane', 'price': 4}, 
            2: {'name':'Pomme', 'price': 2}, 
            3: {'name':'Orange', 'price': 1.5},
            4: {'name':'Poire', 'price': 3}
          }


table = PrettyTable(['Id', 'Name', 'Price'])

for (key,value) in dProduct.items():
   table.add_row([key, value['name'], value['price']])


print(table)


nbreProduit = input("Saisir le nombre de produits à acheter : ")
nbP = int(nbreProduit)

totalPaid = 0.0 #init total


for i in range (0, nbP): #loop pour each product

  productChosen = input("Saisir l'id du produit à ajouter au panier : ")
  pdtCh = int(productChosen)

  try:
    print(table[pdtCh - 1 ]) #table index start with 0

    quantity = input("Saisir une quantité : ")
    q = int(quantity)

    priceProductChosen = dProduct[pdtCh].get('price')
    prPdtCh = float(priceProductChosen)

    priceHT = round((abs(q)*prPdtCh), 2) #prixHT article choose

    totalPaid += priceHT #increment total each time


    itemSelected = dProduct[pdtCh] #get dictionary item key pdtCh value {}
    quantitySelected = quantity.split(':') #get value in input quantity
    quantitySelected = ''.join(quantitySelected) #eject list into str
 

    itemSelected['quantity'] = abs(int(quantitySelected)) #str to number to absolute update dictionary
    itemSelected['totalHT'] = priceHT #update dictionnary


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
  
  priceTTC = totalPaid + (totalPaid * 0.2) #price TTC
  priceTTC = round(priceTTC)
  print('Total TTC : '+ str(priceTTC) + '€')

else:

  remisePrice = round(totalPaid * 0.05, 2) #remise
  print('Remise 5% : '+ str(remisePrice) + '€') 

  priceHTAfter = totalPaid - remisePrice #price after remise
  priceHTAfter = round(priceHTAfter)
  print('Total HT : '+ str(priceHTAfter) + '€') 

  priceTTC = priceHTAfter + (priceHTAfter * 0.2) #price TTC with remise price
  priceTTC = round(priceTTC)
  print('Total TTC : '+ str(priceTTC) + '€')

