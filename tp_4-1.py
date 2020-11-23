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
    print(totalPaid)


  #  totalHT = str(totalHT)
    # print('Total HT : ' + totalHT +'€')


  except IndexError: 
    print("Veuillez saisir un id valide. ")
    break


  except ValueError: 
    print("Veuillez saisir une quantité valide. ")
    break






