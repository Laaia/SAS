#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
line = raw_input()
metodo, e, s = line.split() #Padrão de entrada

try:
	en = open(e, "rb");
	sa = open(s, "rb");
except IOError:
	print "Erro na abertura dos arquivos"

entrada = en.read()
saida = sa.read()

if metodo == 'cesar':
	cesar(entrada, saida)
elif metodo == 'substituicao':
	substituicao(entrada, saida)
elif metodo == 'vigenere':
	vigenere(entrada, saida)
else:
	print "Entrada inválida!"

sa.close()
en.close()
