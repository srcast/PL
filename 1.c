int l1; 
int l2; 
int l3;
int l4;
int i = 0;

printf("Digite o lado 1: \n");
scanf("%i", &l1);

printf("Digite o lado 2: \n");
scanf("%i", &l2);

printf("Digite o lado 3: \n");
scanf("%i", &l3);

printf("Digite o lado 4: \n");
scanf("%i", &l4);

if (l1 == l2){ if (l1 == l3){ if (l1 == l4){printf("Sao os lados de um quadrado\n");i=1;}}}

if (i==0){printf("Nao sao os lados de um quadrado\n");}
