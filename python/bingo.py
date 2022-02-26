import random

numeros = []
while len(numeros) < 90:
    bola = random.randrange(1,91)
    if bola in numeros:
       continue
    numeros.append(bola)
    print ('El...', bola)
print ('Extraccion finalizada, los números han sido...')
print (numeros)
print ('Un total de',len(numeros),'bolas')
print ('Ordenando las bolas de nuevo...')
numeros.sort()
print (numeros)
print ("That's all folks !")
