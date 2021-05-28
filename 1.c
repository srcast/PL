#include <stdio.h>

int main(int argc, char const *argv[])
{
	
	int l1, l2, l3, l4, i;

	printf("Digite o lado 1: ");
	scanf("%i", &l1);

	printf("Digite o lado 2: ");
	scanf("%i", &l2);

	printf("Digite o lado 3: ");
	scanf("%i", &l3);

	printf("Digite o lado 4: ");
	scanf("%i", &l4);

	if (l1 == l2 && l1 == l3 && l1 == l4){
		printf("Sao os lados de um quadrado\n");
	}

	else{
		printf("Nao sao os lados de um quadrado\n");
	}
	
}