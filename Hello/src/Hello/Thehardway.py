'''
Created on 06/11/2012

@author: Michael & Maiken
'''

dariy_section = ['Milk','A38','Ymer',', Le cream Fraise']  
print(dariy_section[0] + dariy_section[3]) 



milk_expiration = (10,28,2012)
print('This milk carton will expire %i %i %i'%(milk_expiration[0] , milk_expiration [1] , milk_expiration[2]))


milk_carton = { 
               'Expiration date':  milk_expiration,
               'fl_oz' : '1L',
               'Cost' : 10,
               'brand_name' : 'Man Milk'
               }
print(milk_carton)

print(milk_carton['Expiration date'], milk_carton['fl_oz'], milk_carton['Cost'], milk_carton['brand_name'])

print(milk_carton.get("Cost")*6)

cheeses = ['Lille bror', 'Gamle Ole', 'Ryge ost']

dariy_section.append(cheeses)

print(dariy_section)

dariy_section.remove(cheeses)

print(dariy_section)

print(len(cheeses))

print(cheeses [0][0:5])