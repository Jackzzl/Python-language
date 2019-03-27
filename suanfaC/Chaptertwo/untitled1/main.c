#include <stdio.h>
#include <string.h>
int main() {
    int count =0;
    char s[20],buf[90];
    scanf("%s",s);
    for(int abc=111;abc<=999;abc++)
        for(int da=11;da<=99;da++){
        int x=abc*(da%10),y=abc*(da/10),z=abc*da;
        sprintf(buf,"%d%d%d%d%d",abc,da,x,y,x);
        int ok=1;
        for(int i=0;i<strlen(buf);i++)
            if(strchr(s,buf[i])==NULL)
                ok=0;
            if(ok) {
                printf("<%d>/n", ++count);
                printf("%5\nX%4d\n-----\n%5d\n%4d\n-----\n%5d\n\n", abc, da, x, y, z);
            }
    }
    printf("The number of sulutions= %d\n",count);
    return 0;
}