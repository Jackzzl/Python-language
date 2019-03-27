#include <stdio.h>
#include <memory.h>
void main()
{
    char a[1000];
    printf("请输入一句话");
    gets(a);
    for(int i=0;i<strlen(a);i++){
        if(a[i-1]=='i'&&a[i]=='s'){
            a[i-1]='I';
            a[i]='S';
        }
    }
    puts(a);
}