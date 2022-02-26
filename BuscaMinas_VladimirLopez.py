import numpy as np  #importamos numpy y le creamos un alias llamado np

File = open('prueba.txt', 'r') #Se usa la función open para abrir un archivo "prueba1.txt"
Mensaje = File.read()    #Se le asigna a var mensaje la lectura del contenido de nuestro archivo

Mensaje = Mensaje.split("\n")   #Divide el contenido de nuestro mensaje en una lista separando el salto de línea (Mensaje-string)
Num = Mensaje[0].split(" ")     #Num va a ser el contenido de nuestro mensaje en una lista separando espacios
Fila = int(Num[0])    #Se toma el primer numero entero de nuestro archivo para el num Filas
Col = int(Num[1])      #Se toma el segundo numero entero de nuestro archivo para el num Columnas

Mensaje.pop(0)      #Se hace pop (se quita) el primer elemento de nuestro contenido en Mensaje

Matrix = []         #Se declara una nueva lista Matrix
Mina = '*'          #Las minas seran representadas por *

for x in range(len(Mensaje)):
  Matrix.append(list(Mensaje[x]))

for i in range(len(Matrix)):
    for j in range (len(Matrix[i])):    
        if('.' == Matrix[i][j]):        #Este ciclo busca en nuestra lista todos los puntos y los cambia por ceros
            Matrix[i][j] = 0
            
for i in range(len(Matrix)):
    for j in range (len(Matrix[i])):
        if('*' == Matrix[i][j]):        #Este ciclo busca en nuestra lista todos los * para detectar donde hay mina
            if (j+1) < Col and (Matrix[i][j+1]) != Mina:    #Busca minas a la derecha donde exista * y evita exceder el valor maximo de la fila
                Matrix[i][j+1] += 1 
                
            if (j-1) >= 0 and (Matrix[i][j-1]) != Mina:     #Busca minas a la izquierda donde exista * y evita exceder el valor maximo de la fila
                Matrix [i][j-1] += 1 
                
            if (i+1) < Fila and  (Matrix[i+1][j]) != Mina:  #Busca minas abajo donde exista * y evita exceder el valor maximo de la fila
                Matrix[i+1][j] += 1 
                
            if (i-1) > 0 and  (Matrix[i-1][j]) != Mina:     #Busca minas arriba donde exista * y evita exceder el valor maximo de la fila
                Matrix[i-1][j] += 1 
                
            if (i-1) > 0 and (j+1) < Col and (Matrix[i-1][j+1]) != Mina:        #Busca minas en la diagonal superior derecha donde exista * y evita exceder el valor maximo de la fila
                Matrix[i-1][j+1] +=1 
                
            if (i-1) >= 0 and (j-1) >= 0 and (Matrix[i-1][j-1]) != Mina:        #Busca minas en la diagonal superior izquierda donde exista * y evita exceder el valor maximo de la fila
                Matrix[i-1][j-1] +=1 
                
            if (i+1) < Fila and (j-1) >= 0 and (Matrix[i+1][j-1]) != Mina:      #Busca minas en la diagonal inferior izquierda donde exista * y evita exceder el valor maximo de la fila
                Matrix[i+1][j-1] +=1 
                
            if (i+1) <= Fila and (j+1) < Col and (Matrix[i+1][j+1]) != Mina:    #Busca minas en la diagonal inferior derecha donde exista * y evita exceder el valor maximo de la fila
                Matrix[i+1][j+1] +=1 
                
for i in range(len(Matrix)):
  for j in range (len(Matrix[i])):
    print(Matrix[i][j], end=" ")    #Imprime el contenido de nuestra matriz
  print("\n")