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

  return priceTTC


def calcRemise(total):
  remisePrice = total * 0.05
  remisePrice = round(remisePrice, 2)
  print('Remise 5% : '+ str(remisePrice) + '€')

  return remisePrice


def calcPriceHTAfter(total, remise):
  priceHTAfter = total - remise
  priceHTAfter = round(priceHTAfter, 2)
  print('Total HT : '+ str(priceHTAfter) + '€')

  return priceHTAfter

