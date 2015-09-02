#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import itertools
from random import randint
from sets import Set
import StringIO
#	FUNCTIONS	#

line = raw_input()
metodo, e = line.split() #Padrão de entrada

try:
    en = open(e, "rb");
    dicionario = open("dic", "rb"); # Dicionário de palavras para busca
    saida = open("saida", "wb")
except IOError:
	print "Erro na abertura dos arquivos"

entrada = en.read()
d = dicionario.readlines()

dic = Set([]) # Inicializa variável para uso de 'hashes'

# Tratamento de dado - Remoção do \n
for i in d:
    dic.add(i.replace("\n", ""))

limit = ['a', 'b', 'c', 'd', '1', '2', '3', '4', '5', '6']

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
def cesar(palavra, chave):
    push = ''
    for x in palavra:
        valor = (ord(x) + chave*(-1)) % 255
        push = push + chr(valor)
    return push

# descriptografa utilizando Vigenere
def vigenere(entrada, chave):
    i = 0	#Indice de controle para posição da chave => i-Modular
    push = ''
    for x in entrada:	#Soma ou diminui a chave do texto entrado
        valor = (ord(x) + ord(chave[(i % len(chave))])*(-1)) % 255
        push = push + chr(valor)
        i += 1
    return push

# descriptografa utilizando Transposição
def transposicao(entrada, chave):
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

def tryTransposicao(entrada):
    for key in range(1, 256):
        texto = transposicao(entrada, key).replace("*", "")  # * => caractere 'null' inserido na criptografia
        if searchWords(texto) >= 90:
            print "Chave = ", key
            saida.write(texto)
            break

def tryCesar(entrada):
    for key in range(1, 256):
        texto = cesar(entrada, key)
        if searchWords(texto) >= 90:
            print "Chave = ", key
            saida.write(texto)
            break

def tryVigenere(entrada):
    key = []
    for i in range(1, len(limit)):
        for a in itertools.permutations(limit, i):
            key = ','.join(a).split(',')
            texto = vigenere(entrada, key)
            if searchWords(texto) >= 90:
                print "Chave = " + ''.join(key)
                saida.write(texto)
                return


#	MAIN	#

if metodo == 'cesar':
	tryCesar(entrada)
elif metodo == 'vigenere':
	tryVigenere(entrada)
elif metodo == 'transposicao':
	tryTransposicao(entrada)
else:
	print "Entrada inválida!"

saida.close()
dicionario.close()
en.close()
