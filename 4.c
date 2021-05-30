


int n[6];
int impares = 0;
int valor;
int i = 0;


printf("Insira os valores: \n");

do{ scanf("%d", &n[i]); i = i + 1; } while (i < 6);


do{ i = i - 1; if((n[i] % 2) == 1){impares = impares + 1; printf("%d\n", n[i]) } } while(i > 0);


printf("impares: %d\n", impares);

