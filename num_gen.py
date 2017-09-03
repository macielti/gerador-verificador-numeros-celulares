#####
#Este programa gera uma lista com todas as possiilidades de numeros de celular
#da operadora da tim registrados na cidade de Gilbués-PI.
#####

#modulo para habilitar o uso de comandos no terminal
import os
#modulo para ser usado no comando de encerramento do programa caso o else da 
#linha 19 seja executado
import sys

#contador que definirá o numero gerado a cada ciclo do loop while
contador= 0
#variavel para armazenar uma versão em srting do numero de telefone
numero= 0
#lista vazia para receber o numero gerado a cada ciclo
lista=[]
#lista usada para armazenar o resultado do comando que verifica quais arquivos 
#temos na pasta principal do programa e verificar se já existe uma lista de
#numeros gerada anteriormente
archiv_list=[]
#armazena o numero final e completo de cada ciclo, pronto para ser adicionado a
#lista
numero_completo=0

#Este comando lê os arquivos existentes na pasta do programa e armazena em uma
#lista
archiv_list = os.listdir()

# verifica se já existe alguma lista de numeros gerado pelo programa 
#anteiormente
if 'numeros.txt' in archiv_list:
    #caso o arquivo já exista o programa exibe uma mensagem de erro programada	
	print('Arquivo numeros.txt já existe, por favor, faça um backup do arquivo\
e exclua o arquivo.')
    #este comando encerra o programa
	sys.exit(0)
#caso o arquivo de numeros.txt não exista ele será criado
else:
	os.system('echo >> numeros.txt')	

#ciclo que será executado pelo numero de combinações possiveis de numeros de
#calular
while contador<999999+1:
   
	#Cada if deste while tem o obejetivo de formatar o numero e adicioná-lo a
	#lista que posteriormente será adicionado ao arquivo com todos os numeros
	#gerados
	if(numero<10):
		numero_completo='89999'+'00000'+str(numero)
		nome= str(numero)+', '
		lista.append(nome+numero_completo)
		print(numero_completo)
		print('Added: '+lista[contador])

	if(9<numero<100):
		numero_completo='89999'+'0000'+str(numero)
		nome= str(numero)+', '
		lista.append(nome+numero_completo)
		print(numero_completo)
		print('Added: '+lista[contador])

	if(99<numero<1000):
		numero_completo='89999'+'000'+str(numero)
		nome= str(numero)+', '
		lista.append(nome+numero_completo)
		print(numero_completo)
		print('Added: '+lista[contador])

	if(999<numero<10000):
		numero_completo='89999'+'00'+str(numero)
		nome= str(numero)+', '
		lista.append(nome+numero_completo)
		print(numero_completo)
		print('Added: '+lista[contador])
	
	if(9999<numero<100000):
		numero_completo='89999'+'0'+str(numero)
		nome= str(numero)+', '
		lista.append(nome+numero_completo)
		print(numero_completo)
		print('Added: '+lista[contador])
	
	if(99999<numero<1000000):
		numero_completo='89999'+str(numero)
		nome= str(numero)+', '
		lista.append(nome+numero_completo)
		print(numero_completo)
		print('Added: '+lista[contador])
    
    #variavel para armazenar uma parcela do numero gerado no ciclo
	numero +=1
	#contador de ciclos
	contador +=1

#cliclo usado para pegar cada numero da lista e escrever em um arquivo de saida
for number in lista:
	os.system('echo '+'"'+number+'"'+' >> '+"numeros.txt")
	print('Número escrito: '+number)

#mensagem de despedida do programa.
print("999999 números gerados.")
