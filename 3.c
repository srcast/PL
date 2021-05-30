int n;
int mul = 1;
int i = 0;
int valor;

printf("Insira um numero: \n");
scanf("%d", &n);

printf("Insira os numeros: \n");

do{scanf("%d", &valor); mul = mul * valor; i = i + 1; } while(i < n);

printf("Resultado: %d ", mul);
	

