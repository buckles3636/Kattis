#include <stdio.h>
#include <stdlib.h>

void main(){
    char input[100];
    double inputint;
    char mw[100];
    
    fgets(input,sizeof(input),stdin);
    inputint = atof(input);
    
    for(int i=1;i<=inputint;i++){
        printf("%d Abracadabra\n",i);
    }

}