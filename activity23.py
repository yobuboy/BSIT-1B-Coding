equips1 = 'Berseker Boots'
equips2 = 'Victory Gloves'
# list with default value
equips = ['Berseker Boots', 'Victory Gloves', 'Slaughterer Helmet', 'Bark Armor', 'Burning Blade', 'Spartan Shield', 'Cloak of Death', 'Pledger\'s Belt', 'Mother Nature', 'Guardian Ring']
print(equips)

# every list has an index value/address
print(equips[3])
print(equips[4: 2])

# appending or adding item on the end of the list
equips.append('Passion Cloak')
print(equips)

# inserting between in a list
equips.insert(4, 'Protector Gloves')
print(equips)

# Removing an Item
equips.pop()
print(equips)

equips.remove('Spartan Shield')
print(equips)

# determining the number of item in the list
print(len(equips))

# sorting
equips.sort()
print(equips)
