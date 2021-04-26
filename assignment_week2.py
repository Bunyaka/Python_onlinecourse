mm_soup = 'minced meat, potatoes, frozen vegetable'
sunday_soup = 'chicken with bones, noodles, soup vegetable'
gulas = 'meat, food cream, potatoes, onion, frozen peas'

print ("What would you like to cook on weekend?")
print ("Here are the options:")
print ("1. Minced Meat Soup")
print ("2. Sunday Soup")
print ("3. Gulas")

choose = int(input())

if choose == 1:
    print ("Buy {}.".format(mm_soup))

elif choose == 2:
    print ("Buy {}.".format(sunday_soup))

elif choose == 3:
    print ("Buy {}.".format(gulas))

else:
    print ("Hmmm. No such food on the list.")