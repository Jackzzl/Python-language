#include <iostream>
#include <cstring>

using namespace std;

const int Len =100024;
char s[Len],t[Len];
int main() {
    while (scanf("%s%s", s, t) == 2) {
        int sLen = strlen(s),tLen = strlen(t);
        bool ok = true;
        for (int i = 0, j = 0; i < sLen; i++, j++) {
            while (j < tLen && t[j] != s[i]) {j++;//不满足条件推出。
            printf("%d,%d\n",i,j);}
            if (j == tLen) { ok = false; break; }
        }
        printf("%s\n", ok ? "Yes" : "No" );
    }
    return 0;
}