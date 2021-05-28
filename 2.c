#include <stdio.h>

int main(int argc, char const *argv[])
{
	
	int n, menor, ncomp, *ar;

	printf("Insira um N: ");
	scanf("%d", &n);
	
	
	printf("Insira um numero: ");
	scanf("%d", &menor);

	
	
	do {
		printf("Insira um numero: ");
		scanf("%d", &ncomp);
		
		if(ncomp < menor){
			menor = ncomp;
		}
		
		n--;
	} while (n > 1);
	
	printf("Menor: %d", menor);
}
