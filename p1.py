import sys

filename = sys.argv[1]
filenameO = filename+'O'

print('Filename:', filename)

file = open(filename+'.txt')

fileo = open(filenameO+'.txt', 'w')

datos = file.read()

print(datos)

datos = datos.replace('\n', ' ')

if '\n' in datos:
 print('si hay')

fileo.write(datos)

fileo.close()

 

