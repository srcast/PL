#include <stdio.h>

int main(int argc, char const *argv[])
{
	int seq[11] = {13, 45, 145, 37, 49, 0, 22, 46, 19, 76, 11, 28};
	int conta = 0, i = 0;

	do{
		
		if(seq[i] % 2 != 0){
			printf("%d ", seq[i]);
			conta += 1;
		}
		

		i++;
	} while(i < (sizeof(seq) / sizeof(seq[0])));
	
	printf("\nImpares: %d\n", conta);

	return 0;
	
}
