# SAS
Diretório para a implementação dos trabalhos de Segurança e Auditoria de Sistemas 

- # T3 - Quebra sem texto em claro

Entrada:
--------
<nome do método> <arquivo criptografado>

Saída:
------
Chave para quebra com o método correspondente


- # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # -

- # T2 - Quebra com texto em claro

Entrada:
--------
<nome do método> <arquivo em claro> <arquivo criptografado>

Saída:
------
Chave para quebra com o método correspondente

- # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # - # -

- # T1 - Implementação de Cifra de César, Transposição, Vigenere e Substituição

<modo> = 1 para criptografar e <modo> = -1 para descriptografar

Cifra de César
---------------
Entrada: cesar <arquivo de entrada> <arquivo de saída> <chave-int> <modo>

Cifra de Transposição
---------------------
Entrada: transposicao <arquivo de entrada> <arquivo de saída> <chave-int> <modo>

Cifra de Vigenere
-----------------
Entrada: vigenere <arquivo de entrada> <arquivo de saída> <chave-str> <modo>

Cifra de Substituição
---------------------
Entrada: substituicao <arquivo de entrada> <arquivo de saída> <arquivo hash> <modo>
