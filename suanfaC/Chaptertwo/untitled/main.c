#include <stdio.h>

int main() {
    int n;
    printf("please write a number(n<20)\n");
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
        for (int a = 0; a <i; a++)
            printf(" ");
        for (int a = 0; a<2*(n-i)-1; a++)
            printf("*");
        /*for (int a = 0; a < n - i; a++)
            printf("2");*/
        printf("\n");
    }
    return 0;
}