#include <stdio.h>
#include <stdlib.h>

void main(){
    int datasets;
    scanf("%i",&datasets);
    for(int i=0;i<datasets;i++){
        int num;
        int days;
        int count = 0;
        scanf("%i %i",&num,&days);
        for(int e=1;e<=days;e++){
            count = (count + e);
        }
        count = count + days;
    printf("%i %i\n",num,count);
    }

}