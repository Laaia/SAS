#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int rg, char *arq[]){
	//arq[] = entrada[1], chave[2], modo[3], saida[4]
	
	FILE *palavra, *saida;
	char x;
	int chave = atoi(arq[2]), valor = 0;

	palavra = fopen(arq[1], "rb");
	saida = fopen(arq[4], "wb");

	if(*arq[3] == '1'){
		while(fscanf(palavra, "%c", &x) !=  EOF){
			valor = (x + chave) % 256;
			fwrite(&valor, sizeof(char), 1, saida);
			printf("%c", valor);
		
		}
	}else{
		while(fscanf(palavra, "%c", &x) !=  EOF){
			valor = (x - chave) % 256;
			fwrite(&valor, sizeof(char), 1, saida);
			printf("%c", valor);
	
		}
	}

	fclose(palavra);
	fclose(saida);

	return 0;
}
