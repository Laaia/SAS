#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import string

line = raw_input()
metodo, e, s = line.split() #Padrão de entrada

try:
	en = open(e, "rb");
	sa = open(s, "rb");
except IOError:
	print "Erro na abertura dos arquivos"

entrada = en.read()
saida = sa.read()

# 	Funções		#

def descriptografar(entrada, chave):
	push = ''
	m = []
	x = 0
	
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
	return push

def comparar(claro, talvez):
	count = 0
	for x in range(0, len(claro)):
		try:
			if claro[x] in talvez[x]:
				count += 1
		except IndexError:
			break
	return (count/len(claro))*100


def transposicao(entrada, saida):
	
	for key in range(1, len(entrada)+1):
		if comparar(entrada, descriptografar(saida, key)) >= 90:
			print "Chave = ", key
			break


def cesar(entrada, saida):
	print "Chave = ", (ord(saida[0]) - ord(entrada[0]))

def vigenere(entrada, saida):
	chave = ''
	for x in range(0, len(entrada)):
		chave += chr(ord(saida[x]) - ord(entrada[x]))
	print "Chave = ", chave

def substituicao(entrada, saida):
	chave = []
	for x in range(0, len(entrada)):
		chave.append( entrada[x]+"->"+ saida[x])
	print "Chave = ", chave
	
#	MAIN	#

if metodo == 'cesar':
	cesar(entrada, saida)
elif metodo == 'substituicao':
	substituicao(entrada, saida)
elif metodo == 'vigenere':
	vigenere(entrada, saida)
elif metodo == 'transposicao':
	transposicao(entrada, saida)
else:
	print "Entrada inválida!"

sa.close()
en.close()
