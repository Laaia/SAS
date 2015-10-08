#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sets import Set
from operator import itemgetter
import itertools


try:
    dic_arq = open("dic.txt", "rb")
except IOError:
    print "Erro na abertura dos arquivos"

dicio = dic_arq.read().split()
dic = Set([])
for i in dicio:
    dic.add(i.replace("\n", ""))

dicP = {} #Dicionário de padrões que aparecem somente uma vez

# Calcula a quantidade de ocorrências de uma string de
# tamanho n em um arquivo de texto
def frequencia(line, modo):
    try:
        tri = open(line+"_"+modo+".txt", "ab")
        dicionario = open(modo+".txt", "rb")
    except IOError:
    	print "Erro na abertura dos arquivos"

    d = dicionario.read()
    d = d.replace("\n", " ")
    d = d.replace("\r", " ")

    i = 0
    f = int(line)
    janela = {}


    while f < len(d):
        janela[d.count(d[i:f])] = d[i:f]
        i += 1
        f += 1

    janela = sorted(janela.items(), key=itemgetter(0), reverse=True)

    strg = ''
    for i in janela:
    	a, b = i
        strg = strg + b + "\n"

    tri.write(strg)

    tri.close()
    dicionario.close()

    print strg

def padrao(palavra):
    letras = {}
    p = ''
    count = 1
    for l in palavra:
        try:
            p += str(letras[l])
        except KeyError:
            p += str(count)
            letras[l] = count
            count += 1

    return p

def padroes(line, modo):
    try:
        s = open("padrao_"+modo+".txt", "wb")
        dicionario = open(line, "r+")
    except IOError:
        print "Erro na abertura dos arquivos"

    d = dicionario.read()

    d = d.replace("\n", " ")
    d = d.replace("\r", " ")

    di = Set(d.split())
    #print dic

    #print "\n\nPadrões: "
    string = ''
    for palavra in di:
    	p = padrao(palavra)
        #print string.count(p)
        dicP[p] = palavra
        string += p + "\n"

    for p in string.split():
        if string.count(p) != 1:
            try:
                del dicP[p]
            except KeyError:
                pass


def searchWords(text):
	hit = 0.0
	lines = 0.0
	text = text.split()
	text = Set(text)
	for word in text:
		if word in dic:
			hit += 1.0
		#print "achei word = " + word
		lines += 1.0
	print (hit/lines)*100
	return (hit/lines)*100
# - - - M A I N - - - #

# Geração de padrões, triplas, duplas e letras com base num dicionario
"""frequencia("1", "dic")
frequencia("2", "dic")
frequencia("3", "dic")"""
padroes("dic.txt","dic")

# Geração de padrões, triplas, duplas e letras com base no texto cifrado
"""frequencia("1", "cif")
frequencia("2", "cif")
frequencia("3", "cif")"""


try:
    lDic = open("1_dic.txt", "rb")
    dDic = open("2_dic.txt", "rb")
    tDic = open("3_dic.txt", "rb")

    lCif = open("1_cif.txt", "rb")
    dCif = open("2_cif.txt", "rb")
    tCif = open("3_cif.txt", "rb")

    cif = open("cif.txt", "rb")
    s = open("saida.txt", "wb")
    tex = open("dic.txt", "rb")
except IOError:
    print "Erro na abertura dos arquivos"


letrasDic = lDic.read()

duplasDic = dDic.read()

triplasDic = tDic.read()

letrasCif = lCif.read()

duplasCif = dCif.read()

triplasCif = tCif.read()


hash = {}
# Associação entre os dados do dicionario com o texto cifrado
# Construção da chave

entrada = cif.read()
texto = tex.read()

i = 0

add = ''
p = '1231452678'
palavra = dicP[p]
for x in range(0, len(entrada)-len(dicP[p])):
    if padrao(entrada[x:x+len(dicP[p])]) == p:
        y = 0
        for a in range(x, x+len(dicP[p])):
            if palavra[y] not in add:
                hash[entrada[a]] = palavra[y]
                add += palavra[y]
            y += 1
        break
p = '1223455666738910117121387'
palavra = dicP[p]
for x in range(0, len(entrada)-len(dicP[p])):
    if padrao(entrada[x:x+len(dicP[p])]) == p:
        y = 0
        for a in range(x, x+len(dicP[p])):
            if palavra[y] not in add:
                hash[entrada[a]] = palavra[y]
                add += palavra[y]
            y += 1
        break
p = '12334546478'
palavra = dicP[p]
for x in range(0, len(entrada)-len(dicP[p])):
    if padrao(entrada[x:x+len(dicP[p])]) == p:
        y = 0
        for a in range(x, x+len(dicP[p])):
            if palavra[y] not in add:
                hash[entrada[a]] = palavra[y]
                add += palavra[y]
            y += 1
        break
p = '123456789109119812'
palavra = dicP[p]
for x in range(0, len(entrada)-len(dicP[p])):
    if padrao(entrada[x:x+len(dicP[p])]) == p:
        y = 0
        for a in range(x, x+len(dicP[p])):
            if palavra[y] not in add:
                hash[entrada[a]] = palavra[y]
                add += palavra[y]
            y += 1
        break
p = '12345675389101112'
palavra = dicP[p]
for x in range(0, len(entrada)-len(dicP[p])):
    if padrao(entrada[x:x+len(dicP[p])]) == p:
        y = 0
        for a in range(x, x+len(dicP[p])):
            if palavra[y] not in add:
                hash[entrada[a]] = palavra[y]
                add += palavra[y]
            y += 1
        break
p = '1234546781798610'
palavra = dicP[p]
for x in range(0, len(entrada)-len(dicP[p])):
    if padrao(entrada[x:x+len(dicP[p])]) == p:
        y = 0
        for a in range(x, x+len(dicP[p])):
            if palavra[y] not in add:
                hash[entrada[a]] = palavra[y]
                add += palavra[y]
            y += 1
        break
p = '12345678291011121213141515'
palavra = dicP[p]
for x in range(0, len(entrada)-len(dicP[p])):
    if padrao(entrada[x:x+len(dicP[p])]) == p:
        y = 0
        for a in range(x, x+len(dicP[p])):
            if palavra[y] not in add:
                hash[entrada[a]] = palavra[y]
                add += palavra[y]
            y += 1
        break
p = '12234553678910111265913141512816171614610'
palavra = dicP[p]
for x in range(0, len(entrada)-len(dicP[p])):
    if padrao(entrada[x:x+len(dicP[p])]) == p:
        y = 0
        for a in range(x, x+len(dicP[p])):
            if palavra[y] not in add:
                hash[entrada[a]] = palavra[y]
                add += palavra[y]
            y += 1
        break
p = '12234556667892101112101387141385155165175151617165'
palavra = dicP[p]
for x in range(0, len(entrada)-len(dicP[p])):
    if padrao(entrada[x:x+len(dicP[p])]) == p:
        y = 0
        for a in range(x, x+len(dicP[p])):
            if palavra[y] not in add:
                hash[entrada[a]] = palavra[y]
                add += palavra[y]
            y += 1
        break

for x in range(0, 12):
    if duplasDic[x] not in add:
        hash[triplasCif[x]] = triplasDic[x]
        add += triplasDic[x]

for x in range(0, 6):
    if duplasDic[x] not in add:
        hash[duplasCif[x]] = duplasDic[x]
        add += duplasDic[x]

for x in range(0, 5):
    if letrasDic[x] not in add:
        hash[letrasCif[x]] = letrasDic[x]
        add += letrasDic[x]

print hash
print "--"*8

hash[letrasCif[0]] = letrasDic[0]

saida = ''
for i in entrada:
    try:
        saida += hash[i]
    except KeyError:
        saida += '_'



searchWords(saida)

s.write(saida)
