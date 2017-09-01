import os

contador= 0
numero= 0
lista=[]
while contador<999999+1:
	

	if(numero<10):
		lista.append('00000'+str(numero))		
		print(lista[contador])

	if(9<numero<100):
		lista.append('0000'+str(numero))		
		print(lista[contador])

	if(99<numero<1000):
		lista.append('000'+str(numero))		
		print(lista[contador])

	if(999<numero<10000):
		lista.append('00'+str(numero))
		print(lista[contador])
	
	if(9999<numero<100000):
		lista.append('0'+str(numero))
		print(lista[contador])
	
	if(99999<numero<1000000):
		lista.append(str(numero))
		print(lista[contador]) 

	numero +=1
	contador +=1
	
	
	





