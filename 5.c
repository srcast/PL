int n[5];

int i = 0;

printf("Insira os valores: \n");

do{ scanf("%d", &n[i]); i = i + 1; } while (i < 5);

do{ i = i - 1; printf("valor: %d \n", n[i]); printf("\n"); } while(i > 0);
