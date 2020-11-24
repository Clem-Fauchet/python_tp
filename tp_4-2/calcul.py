# -*- coding: utf-8 -*-
#!/usr/bin/python
import main

def calcPriceHT(quantity, productChosen):
    priceHT = (abs(quantity) * productChosen)
    priceHT = round(priceHT, 2)

    return priceHT

