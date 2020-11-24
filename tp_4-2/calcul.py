# -*- coding: utf-8 -*-
#!/usr/bin/python

def calcPriceHT(quantity, productChosen):
  priceHT = (abs(quantity) * productChosen)
  priceHT = round(priceHT, 2)

  return priceHT


def calcPriceTTC(total):
  priceTTC = total + (total * 0.2)
  priceTTC = round(priceTTC, 2)
  print('Total TTC : '+ str(priceTTC) + '€')


def calcRemise(total):
  remisePrice = round(total * 0.05, 2) 
  print('Remise 5% : '+ str(remisePrice) + '€')


def calcPriceHTAfter(total, remise)
  priceHTAfter = total - remise
  priceHTAfter = round(priceHTAfter)
  print('Total HT : '+ str(priceHTAfter) + '€')

