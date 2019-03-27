#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <w32api/wsman.h>
#include <w32api/d2d1helper.h>

const char* rev="A   3  HIL  JM 0  2TUVWXY51SE  Z  8";
const char* mag[]={"not a palindrome","a regular palinderome","a mirrored string","a mirrored palindrome"};


int main() {
    char s[30];
    while(scanf("%s",s)==1) {
        int len = strlen(s);
        int p = 1, m = 1;
        for (int i = 0; i < (len + 1) / 2; i++) {
            if (s[i] != s[len - 1 - i])
                p = 0;//非回文数
            if (r(s[i]) != s[len - 1 - i])
                m = 0;//不是镜像
        }
        printf("%s--is %s.\n\n", s, mag[m * 2 + p]);
    }
    return 0;
}