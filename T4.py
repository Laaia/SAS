#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sets import Set
from operator import itemgetter

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

    dic = Set(d.split())
    #print dic

    #print "\n\nPadrões: "
    string = ''
    dicPadroes = {}
    for palavra in dic:
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
    s = open("saida.txt", "ab")
except IOError:
    print "Erro na abertura dos arquivos"


letrasDic = lDic.read().split()

duplasDic = dDic.read().split()
#duplasDic = duplasDic[::-1].split()

triplasDic = tDic.read().split()
#triplasDic = triplasDic[::-1].split()

letrasCif = lCif.read().split()
#letrasCif = letrasCif[::-1].split()

duplasCif = dCif.read().split()
#letrasCif = duplasCif[::-1].split()

triplasCif = tCif.read().split()


hash = {}
# Associação entre os dados do dicionario com o texto cifrado
# Construção da chave

for i in xrange(len(triplasDic)-1, 0, -2):
	#print triplasDic[i]+" "+ triplasCif[i]
	for (x, y) in zip(triplasDic[i], triplasCif[i]):
		hash[x] = y
		#hash[x].append(y)

for i in xrange(len(duplasDic)-2, 0, -2):
	#print duplasDic[i]+" "+ duplasCif[i]
	for (x, y) in zip(duplasDic[i], duplasCif[i]):
		if x not in hash:
			hash[x] = y

"""for i in xrange(1, len(letrasDic), 2):
	x, y = letrasDic[len(letrasDic) - (i+1)], letrasCif[len(letrasCif) - i]
	#print x+" "+y
	if x not in hash:
		hash[x] = y
"""
entrada = cif.read()
print hash

# Quebra do texto cifrado
for i in hash:
	#print hash[i]+" "+ i
	entrada = entrada.replace(hash[i], i)

s.write(entrada)

#quanto de cada pegar: I'm god!
