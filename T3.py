#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

from random import randint
from sets import Set
import StringIO
#	FUNCTIONS	#

line = raw_input()
metodo, e = line.split() #Padrão de entrada

#Força bruta em chave - A cada chave testada verificar no dicionário
#Se é um texto claro

try:
    en = open(e, "rb");
    dicionario = open("dic", "rb");
    saida = open("saida", "wb")
except IOError:
	print "Erro na abertura dos arquivos"

entrada = en.read()
d = dicionario.readlines()
dic = Set([])

# Tratamento de dado - Remoção do \n
for i in d:
    dic.add(i.replace("\n", ""))
dic = Set(dic)


#Função que verifica a pertinência do arquivo descriptografado
def searchWords(text):
    hit = 0.0
    lines = 0.0
    text = text.split()
    text = Set(text)
    for word in text:
        if (word in dic) or (word.lower() in dic):
            hit += 1.0
            #print "achei word = " + word

        lines += 1.0

    return (hit/lines)*100

# descriptografa utilizando César
def tryCesar(palavra, chave):
    push = ''
    for x in palavra:
        valor = (ord(x) + chave*(-1)) % 255
        push = push + chr(valor)
    return push

# descriptografa utilizando Vigenere
def tryVigenere(entrada, chave):
    i = 0	#Indice de controle para posição da chave => i-Modular
    push = ''
    for x in entrada:	#Soma ou diminui a chave do texto entrado
        valor = (ord(x) + chave*(-1)) % 255
        push = push + chr(valor)
        i += 1
    return push

# descriptografa utilizando Transposição
def tryTransposicao(entrada, chave):
    push = ''
    m = []
    x = 0

    chave = len(entrada)/float(chave)

    if len(entrada) <= chave:
        ji = 1			#Chave maior => entrada cabe em uma linha
        chave = len(entrada)	#Correção para o indice dentro da linha
    else:

        ji = math.ceil(len(entrada)/float(chave))

    for j in range(0, int(ji)):		#Linha x Coluna
        m.append([])
        for i in xrange(0, int(chave)):
            m[j].append([])
            m[j][i] = '\r'
            if x < len(entrada):
                m[j][i] = entrada[x]
            x += 1		# x = índice do caractere do vetor de entrada

    m = zip(*m)				#Transposta da matriz
    x = 0
    for j in xrange(0, int(chave)):		#Leitura da transposta para obtenção do texto final
        for i in xrange(0, int(ji)):
            #print push
            push = push + m[j][i]
    return push

def transposicao(entrada):
    for key in range(1, 256):
        texto = tryTransposicao(entrada, key)
        #   print texto
        texto = texto.replace("*", "")
        if searchWords(texto) >= 90:
            print "Chave = ", key
            saida.write(texto)
            break

def cesar(entrada):
    for key in range(1, 256):
        texto = tryCesar(entrada, key)
        if searchWords(texto) >= 90:
            print "Chave = ", key
            saida.write(texto)
            break

def vigenere(entrada):
    for key in range(0, 256):
        texto = tryVigenere(entrada, key)
        if searchWords(texto) >= 90:
            print "Chave = " + chr(key)
            saida.write(texto)
            break



#	MAIN	#

if metodo == 'cesar':
	cesar(entrada)
elif metodo == 'vigenere':
	vigenere(entrada)
elif metodo == 'transposicao':
	transposicao(entrada)
else:
	print "Entrada inválida!"

saida.close()
dicionario.close()
en.close()
