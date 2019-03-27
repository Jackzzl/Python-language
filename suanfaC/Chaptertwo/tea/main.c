#include <stdio.h>
#include<math.h>
#include <string.h>
#define max 1000
int a[max];
int main() {
    int n,k,first=1;
    memset(a,0, sizeof(a));
    printf("please input two number");
    scanf("%d%d",&n,&k);
    for(int i=1;i<=k;i++)
        for(int b=1;b<=n;b++){
        if(b%i==0)
            a[b]=!a[b];
    }
    for(int i=1;i<=n;i++)
        if(a[i]){
        if(a[i]==0)
            if(first) first=0; else printf(" ");
            printf("%d",i);
    }
    printf("\n");
    return 0;
}