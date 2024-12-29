from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

print('I2C SCANNER')
devices = i2c.scan()

if len(devices) == 0:
  print("Aucun composant i2c trouvé !")
else:
  print(len(devices),' composant(s) i2C trouvé(s) :')
  for device in devices:
    print("Adresse I2C hexadécimale : ", hex(device))
