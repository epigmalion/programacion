fichero = open('intro.txt')
palabras = dict()
for line in fichero:
    line = line.rstrip()
    words = line.split()
    for word in words:
        
        
