#include <stdio.h>

int main() {
    int a1,a2,b1,b2,c1,c2;
    printf("case 1:please input three number\n");
    scanf("%d%d%d",&a1,&b1,&c1);
    printf("case 2:please input three number\n");
    scanf("%d%d%d",&a2,&b2,&c2);
    for(int n=10;n<=100;n++){
        if(n%3==a1&&n%5==b1&&n%7==c1){
            printf("Case 1: %d\n",n);
            break;
        }
        if(n==100)
            printf("Case 1: no answer\n");}
    for(int n=10;n<=100;n++){
        if(n%3==a2&&n%5==b2&&n%7==c2) {
            printf("Case 2: %d\n", n);
            break;
        }
        if(n==100)
            printf("Case 2: no answer\n");
    }
    return 0;
}