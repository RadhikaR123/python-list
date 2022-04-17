name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]
z = zip(name, animal, age)
#=> <zip at 0x111081e48>
for name,animal,age in z:
    print("%s the %s is %s" % (name, animal, age))
