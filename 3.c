int n;
int mul = 1;
int i = 0;
int valor;
printf("Insira um numero: ");
scanf("%d", &n);
do{
printf("Insira um valor: ");
scanf("%d", &valor);
mul = mul * valor;
i = i + 1;
} while(i < n);
printf("Resultado: %d\n", mul);
	

