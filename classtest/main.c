#include <stdio.h>

int main() {
    int count=0;
    char ch;
    printf("please intput characters:");
    for(;(ch=getchar())!='\n';){
        if(ch>='A'&&ch<='Z')
            count++;
    }
    printf("count=%d\n",count);
    return 0;
}