# -*- coding: utf-8 -*-
#!/usr/bin/python

class Caisse:

  def __init__(self, priceHT, priceTTC, remise, priceTTCAfter, has_Paid ):
    self.priceHT = priceHT
    self.priceTTC = priceTTC
    self.remise = remise
    self.priceTTCAfter = priceTTCAfter
    self.has_Paid = has_Paid