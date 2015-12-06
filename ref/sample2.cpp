#include <stdio.h>
#include <stdlib.h>
#include <string>

void sample(char *p);

int main(int argc,char *argv[])
{
	int i;

	printf("cout of argc = %d\n", argc);
	for (i = 0; i < argc; i++) {
		printf("argv[%d] = %s\n", i, argv[i]);
	}

	sample(argv[1]);

}

void sample(char *p){
	printf("sample param; %s\n", p);

}
