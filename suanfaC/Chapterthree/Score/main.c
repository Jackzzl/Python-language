#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//
int main() {
    while (1) {
        char ch[85];
        int cunter, sum;
        int i, a;
        printf("plaese intput the string!\n");
        scanf("%s",ch);
        int len=strlen(ch);
        for(int a=0;a<len;a++){
            if (ch[a] == 'O') {
                cunter += 1;
            }
            else if (ch[a]== 'X') {
                i += 1;
                cunter = 0;
            }
            else {
                printf("error input\n");
                break;
            }
            sum = cunter + sum;
        }
        printf("The result is %d", sum);
        return 0;
    }
}