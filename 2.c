int n;
int menor;
int ncomp;

printf("Insira um N: \n");
scanf("%d", &n);
	
	
printf("Insira os numeros: \n");
scanf("%d", &menor);

n = n - 1;

do { scanf("%d", &ncomp); if(ncomp < menor){ menor = ncomp; } n = n - 1;} while (n > 0);
	
printf("Menor: %d ", menor);
