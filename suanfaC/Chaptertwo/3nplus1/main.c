#include <stdio.h>
#include <math.h>
int main() {
    int n2,count;
    printf("please write a number\n");
    scanf("%d",&n2);
    long long n=n2;
    while(n>1){
        if(n%2==0)
        {n=n/2;
        count++;}
        else {
            n = 3 * n + 1;
            count++;
        }
    }
    printf("%d, %d\n",n,count);
    return 0;
}