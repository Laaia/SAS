#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from random import randint
#	FUNCTIONS	#

line = raw_input()

def cesar(palavra, saida, chave, modo):
	push = ''
	for x in palavra:
		valor = (ord(x) + chave*modo) % 255
		push = push + chr(valor)	#Concatena caractere por caractere para uma única gravação
	saida.write(push)
	print "Saída com César:\n" + '-'*10 + '\n'+ push

def transposicao(entrada, saida, chave, modo):
	push = ''
	m = []
	x = 0
	if modo == (-1):			#modo = -1 => Criptografar => Chave = inverso
		chave = len(entrada)/chave
	
	if len(entrada) <= chave:
		ji = 1			#Chave maior => entrada cabe em uma linha
		chave = len(entrada)	#Correção para o indice dentro da linha
	else:
		ji = math.ceil(len(entrada)/float(chave))

	for j in range(0, int(ji)):		#Linha x Coluna
		m.append([])
		for i in xrange(0, chave):
			m[j].append([])
			m[j][i] = '\r'
			if x < len(entrada):
				m[j][i] = entrada[x]
			x += 1		# x = índice do caractere do vetor de entrada

	m = zip(*m)				#Transposta da matriz
	x = 0
	for j in xrange(0, chave):		#Leitura da transposta para obtenção do texto final
		for i in xrange(0, int(ji)):
			#print push
			push = push + m[j][i]

	saida.write(push)
	print "Saída com Transposição:\n" + '-'*10 + '\n'+ push

def vigenere(entrada, saida, chave, modo):
	i = 0	#Indice de controle para posição da chave => i-Modular
	push = ''
	for x in entrada:	#Soma ou diminui a chave do texto entrado
		valor = ord(x) + ord(chave[(i % len(chave))])*modo
		push = push + chr(valor)
		i += 1
	saida.write(push)
	print "Saída com Vigenere:\n" + '-'*10 + '\n'+ push

def doHash(chave):
	push = ''
	try:
		hash = open(chave, "wrb");	
	except IOError:
		print "Erro na abertura do arquivo: Chave!"

	vector = []

	for x in xrange(0, 256):	#Preenche com valores de 0 a 255
		vector.append(x)

	for x in xrange(0, 256):
		j = randint(0, len(vector)-1)
		#print "len = ", len(vector)
		#print "j = ", j
		push = push + chr(vector[j]) + '\r\n'
		vector.pop(j)

	hash.write(push)
	hash.close()

def substituicao(entrada, saida, chave, modo):
	push = ''
	h = ''
	if modo == 1:
		doHash(chave)
	try:
		h = open(chave, "rb+");	
	except IOError:
		print "Erro na abertura do arquivo: Chave!"
	hash = h.read()
	hash = hash.split("\r\n")
	hash.pop(len(hash)-1)
	
	if modo == 1:
		for x in entrada:
			push += hash[ord(x)]
	else:
		for x in entrada:
			push += chr(hash.index(x))

	saida.write(push)
	print "Saída com Substituição:\n" + '-'*10 + '\n'+ push
			
		
#	MAIN	#
metodo, e, s, chave, modo = line.split() #Padrão de entrada 
#Nome da cifra, arquivo de entrada, arquivo de saida, chave e modo(Criptografar(1), Descriptografar(-1))


try:
	entrada = open(e, "rb");
	saida = open(s, "wb");
except IOError:
	print "Erro na abertura dos arquivos"

a = entrada.read()			#Adiciona todo conteúdo do arquivo em um vetor
print "Entrada:\n" + '-'*10 + '\n' + a


if metodo == 'cesar':
	cesar(a, saida, int(chave), int(modo))
elif metodo == 'transposicao':
	transposicao(a, saida, int(chave), int(modo))
elif metodo == 'vigenere':
	vigenere(a, saida, chave, int(modo))
elif metodo == 'substituicao':
	substituicao(a, saida, chave, int(modo))

saida.close()
entrada.close()
