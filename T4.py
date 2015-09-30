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

    janela = sorted(janela.items(), key=itemgetter(0))

    strg = ''
    for i in janela:
    	a, b = i
        strg = strg + str(a) + " " + b + "\n"

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
        s = open("padrao_"+modo+".txt", "ab")
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
    dicPadroes = {}
    for palavra in di:
    	p = padrao(palavra)
        string += p + "\n"
        dicPadroes[p] = string.count(p+"\n")

    #print string
    dicPadroes = sorted(dicPadroes.items(), key=itemgetter(1))

    strg = ''
    for i in dicPadroes:
    	a, b = i
        strg = strg + str(a) + " " + str(b) + "\n"
    print strg
    s.write(strg)
    s.close()

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
    #print (hit/lines)*100
    return (hit/lines)*100
# - - - M A I N - - - #

# Geração de padrões, triplas, duplas e letras com base num dicionario
"""frequencia("1", "dic")
frequencia("2", "dic")
frequencia("3", "dic")
padroes("dic.txt","dic")"""

# Geração de padrões, triplas, duplas e letras com base no texto cifrado
"""frequencia("1", "cif")
frequencia("2", "cif")
frequencia("3", "cif")
padroes("cif.txt","cifra")"""


try:
    lDic = open("1_dic.txt", "r+")
    dDic = open("2_dic.txt", "r+")
    tDic = open("3_dic.txt", "r+")

    lCif = open("1_cif.txt", "r+")
    dCif = open("2_cif.txt", "r+")
    tCif = open("3_cif.txt", "r+")

    cif = open("cif.txt", "r+")

except IOError:
    print "Erro na abertura dos arquivos"


letrasDic = lDic.read().split()

duplasDic = dDic.read().split()

triplasDic = tDic.read().split()

letrasCif = lCif.read().split()

duplasCif = dCif.read().split()

triplasCif = tCif.read().split()


hash = {}
# Associação entre os dados do dicionario com o texto cifrado
# Construção da chave

#hash[' '] = letrasCif[len(letrasCif) - 1]

add = ''
for i in xrange(1, 10, 2):
    #print triplasDic[i]+" "+ triplasCif[i]
    for (x, y) in zip(triplasCif[len(triplasCif)-i], triplasDic[len(triplasDic)-i]):
        #print "x = "+x+" y = "+y
        if y not in add:
            hash[x] =[]
            hash[x].append(y)
            add += y

for i in xrange(1, 10, 2):
    #print duplasDic[i]+" "+ duplasCif[i]
    for (x, y) in zip(triplasCif[len(triplasCif)-i], triplasDic[len(triplasDic)-i]):
        if y not in add:
            hash[x] = []
            hash[x].append(y)

for i in xrange(1, 10, 2):
    x, y = letrasCif[len(letrasCif) - i], letrasDic[len(letrasDic) - (i+1)]
    #print x+" "+y
    if y not in add:
        hash[x] = []
        hash[x].append(y)

entrada = cif.read()
hash[letrasCif[len(letrasCif)-1]].append(" ")
for h in hash:
    print hash[h]
itr = 0
print dic
while itr < len(hash):
	key = ''
	for x in hash:
		lista = hash[x]
		try:
			key += lista[itr]
		except IndexError:
			pass
	for a in itertools.permutations(key, len(key)):
		l = 0
		#print a
		# Quebra do texto cifrado
		for i in hash:
			try:
				entrada = entrada.replace(i, key[l])
			except IndexError:
				pass
			l += 1
		if searchWords(entrada) >= 50:
			print "Chave = " + key
			s.write(entrada)
			break
	itr += 1
