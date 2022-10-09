#include <stdio.h>
#include <stdlib.h>

void main(){
    
    int articles;
    int impact;
    int total;

    scanf("%i %i",&articles,&impact);
    //printf("articles %i\n",articles);
    //printf("impact %i\n",impact);
    total = ((articles * (impact-1))+1);
    printf("%i",total);
 

}