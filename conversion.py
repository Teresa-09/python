#include<stdio.h>
int main()
{
    int centimeter,meter, kilometer;
    printf(" ");
    scanf("%d",& kilometer);
    meter=kilometer*1000;
    centimeter=kilometer*100000;
    printf("\n %d",meter);
    printf("\n %d", centimeter);
    return 0;
}
