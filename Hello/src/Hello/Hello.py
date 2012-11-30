'''
Created on 01/11/2012

@author: Michael & Maiken
'''
def BuyBread():
    print("Buying Bread...")
    return "Bread"

def BuyButter():
    return "Butter"


Food = []

Food.append(  BuyButter())
Food.append(  BuyBread())

print (Food)

