#include <stdio.h>
#include <string.h>
#define maxn 105

int less(const char *s,int p,int q){
    int n=strlen(s);
    for(int i=0;i<n;i++){
        if(s[(p+i)%n]!=s[(q+i)%n]) {
            printf("%d%d\n",p,q);
            return s[(p + i) % n] < s[(q + i) % n];
           // printf("%d",p);
        }
    }
    return 0;
}

int main() {
    int T;
    char s[maxn];
    printf("输入次数:\n");
    scanf("%d",&T);
    while(T--){
        printf("输入要排列的字符串:\n");
        scanf("%s",s);
        int ans=0;
        int n=strlen(s);
        for(int i=0;i<n;i++)
            if(less(s,i,ans))
                ans=i;
        for(int i=0;i<n;i++)
            putchar(s[(i+ans)%n]);
        putchar('\n');
    }
    return 0;
}